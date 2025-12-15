# -*- coding: utf-8 -*-
"""
Script to convert straight quotation marks to Chinese curly quotation marks.
Processes all .tex files in the zh-CN directory.

Rules:
- "..." -> "..."  (straight double quotes to Chinese double quotes)
- '...' -> '...'  (straight single quotes to Chinese single quotes, but careful with LaTeX)
"""

import os
import re
import sys

def convert_quotes(text):
    """
    Convert straight quotes to Chinese curly quotes.
    This is tricky because we need to:
    1. Avoid converting quotes inside LaTeX commands
    2. Pair opening and closing quotes correctly
    """
    result = []
    i = 0
    in_math = False
    in_verb = False

    while i < len(text):
        char = text[i]

        # Track math mode
        if char == '$' and (i == 0 or text[i-1] != '\\'):
            in_math = not in_math
            result.append(char)
            i += 1
            continue

        # Skip if in math mode
        if in_math:
            result.append(char)
            i += 1
            continue

        # Check for verbatim environments
        if text[i:i+6] == '\\verb':
            # Find the delimiter and skip until closing
            j = i + 5
            if j < len(text):
                delim = text[j]
                result.append(text[i:j+1])
                j += 1
                while j < len(text) and text[j] != delim:
                    result.append(text[j])
                    j += 1
                if j < len(text):
                    result.append(text[j])
                    j += 1
                i = j
                continue

        # Handle straight double quote
        if char == '"':
            # Look back to determine if opening or closing
            # Opening: after space, newline, punctuation, or start
            # Closing: after letter, number, or Chinese character
            prev_char = text[i-1] if i > 0 else ' '

            # Check if this is likely an opening quote
            if prev_char in ' \t\n\r（([{、，。！？；：' or i == 0:
                result.append('"')  # Opening Chinese quote
            else:
                result.append('"')  # Closing Chinese quote
            i += 1
            continue

        # Regular character
        result.append(char)
        i += 1

    return ''.join(result)


def process_file(filepath):
    """Process a single .tex file."""
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count original straight quotes
    original_count = content.count('"')

    if original_count == 0:
        print(f"  No straight quotes found.")
        return 0

    # Convert quotes
    new_content = convert_quotes(content)

    # Count remaining straight quotes (should be 0 ideally)
    remaining = new_content.count('"')
    converted = original_count - remaining

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Converted {converted} quote marks, {remaining} remaining.")
    return converted


def main():
    """Main function to process all .tex files."""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Find all .tex files
    tex_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.tex'):
                tex_files.append(os.path.join(root, file))

    total_converted = 0
    for filepath in tex_files:
        total_converted += process_file(filepath)

    print(f"\nTotal: Converted {total_converted} quote marks across {len(tex_files)} files.")


if __name__ == '__main__':
    main()
