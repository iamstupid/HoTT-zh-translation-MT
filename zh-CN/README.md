# 同伦类型论 (HoTT) 中文翻译项目

《Homotopy Type Theory: Univalent Foundations of Mathematics》中文翻译

## 项目概述

本项目旨在将同伦类型论教科书翻译成中文，使中文读者能够学习这一数学基础的前沿领域。

原书是2012/13年在普林斯顿高等研究院进行的"数学泛等基础"（Univalent Foundations）项目的成果。

## 许可证

本翻译遵循原书的 [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/)。

## 目录结构

```
zh-CN/
├── chapters/           # 章节翻译
│   ├── introduction.tex
│   ├── preliminaries.tex   (第1章 类型论)
│   ├── basics.tex          (第2章 同伦类型论)
│   ├── logic.tex           (第3章 集合与逻辑)
│   ├── equivalences.tex    (第4章 等价)
│   ├── induction.tex       (第5章 归纳)
│   ├── hits.tex            (第6章 高阶归纳类型)
│   ├── hlevels.tex         (第7章 同伦n-类型)
│   ├── homotopy.tex        (第8章 同伦论)
│   ├── categories.tex      (第9章 范畴论)
│   ├── setmath.tex         (第10章 集合论)
│   └── reals.tex           (第11章 实数)
├── frontmatter/        # 前言部分
│   ├── front.tex
│   └── preface.tex
├── backmatter/         # 附录部分
│   ├── formal.tex
│   └── symbols.tex
├── glossary.tex        # 术语表
├── macros-zh.tex       # 中文宏定义
└── main-zh.tex         # 中文版主文件
```

## 翻译进度

详见 [PROGRESS.md](PROGRESS.md)

## 编译方法

确保安装了支持中文的 LaTeX 发行版（如 TeXLive 或 MiKTeX），并安装 ctex 宏包。

```bash
# 编译中文版
make hott-zh.pdf
```

## 参与翻译

1. 阅读 [翻译指南](TRANSLATION_GUIDE.md)
2. 查看 [术语表](glossary.tex) 确保术语一致性
3. 选择未翻译的章节开始工作
4. 提交 Pull Request

## 术语约定

请参考 [glossary.tex](glossary.tex) 中的标准术语翻译。

## 联系方式

如有问题，请在 GitHub Issues 中提出。
