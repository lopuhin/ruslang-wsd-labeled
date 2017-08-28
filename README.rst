Labeled Russian Context for WSD
===============================

Contexts sampled from RuTenTen and RNC. Sense definitions from Active Dictionary.
Some words have two annotators. Number of contexts is 100 for most words
and 500 for 7 words.

Annotators (words):

- Анастасия Лопухина (47)
- Константин Лопухин (11)
- Александра Удальцова (2)
- Анастасия К. (2)
- Анна Кот (2)
- Анна Татаренко (2)
- Борис Иомдин (2)
- Иван Самойленко (1)

Contexts are stored in ``rl_wsd_labeled/``::

    rl_wsd_labeled
    ├── adjectives
    │   └── RuTenTen
    ├── nouns
    │   ├── RNC
    │   └── RuTenTen
    └── verbs
        └── RuTenTen

A python interface is provided. Intall the package first::

    pip install rl_wsd_labeled

and then in order to get labeled contexts::

    >>> import rl_wsd_labeled
    >>> f = rl_wsd_labeled.contexts_filename('nouns', 'RuTenTen', 'горшок')
    >>> rl_wsd_labeled.get_contexts(f)

    ({'1': 'Округлый глиняный сосуд для приготовления пищи (печной горшок)',
      '2': 'Расширяющийся кверху сосуд с отверстием в дне (цветочный горшок)',
      '3': 'Ночной горшок'},
     [(('телевизор, - ковер, , - музыкальный центр, - стол, - аквариум, - 3 шкафа, - цветы в',
        ' горшках',
        ', - мелкие аксессуары.'),
      '2'),
      ...
      (('ибо настанет срок и оно будет разрушено течением времени либо войною, будто старый',
        ' горшок',
        ' с вином в трюме торгового корабля, попавшего в бурю и разбившегося о скалы.'),
      '1')
     ])

Apart from senses, there are two special annotations: "0" means
"I don't know/the context is unclear/the contexts is invalid", and "max sense + 1"
mean "other sense, not listed among given senses". Contexts marked as "0" or "other"
are not returned, unless ``with_skipped=True`` is passed.
If there was more then one annotator, contexts where annotators did not agree are also
not included. There is a function ``rl_wsd_labeled.get_agreement`` that returns the
ratio of senses where where both annotators gave either the
same concrete sense, or both skipped the senses (so "0" and "other" are considered equal).
