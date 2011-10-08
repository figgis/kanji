#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import codecs
import unicodedata
from string import Template

out = codecs.getwriter('utf-8')(sys.stdout)

tmp=r'''
\documentclass[avery5371,grid,frame]{flashcards}
\usepackage{fontspec}
\setmainfont{Sazanami Mincho}

\cardfrontstyle[\large\slshape]{headings}
\cardbackstyle{empty}
\begin{document}
\cardfrontfoot{Genki I}
'''

card_template=Template(r'''
\begin{flashcard}[lesson\ $lesson]{\Huge{$kanji}}
%\medskip
\large{$definition}\\
\large{$reading}\\
\scriptsize{$example}
\end{flashcard}
''')

latex_pre=unicode(tmp, 'utf-8')

del tmp

latex_post=r'''
\end{document}
'''
