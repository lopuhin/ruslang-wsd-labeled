Labeled Russian Context for WSD
===============================

Contexts sampled from RuTenTen and RNC. Sense definitions from Active Dictionary.
Some words have two annotators. Number of contexts is 100 for most words
and 500 for 7 words.

Annotators (words):

- Анастасия Лопухина (23)
- Константин Лопухин (11)
- Александра Удальцова (2)
- Анастасия К. (2)
- Анна Кот (2)
- Анна Татаренко (2)
- Борис Иомдин (2)
- Иван Самойленко (1)

Contexts are stored in ``rl_wsd_labeled/``::

    rl_wsd_labeled
    ├── nouns
    │   ├── RNC
    │   └── RuTenTen
    └── verbs
        └── RuTenTen

A python interface is provided. Intall the package first, and then::

    >>> import rl_wsd_labeled
    >>> f = rl_wsd_labeled.contexts_filename('nouns', 'RuTenTen', 'горшок')
    >>> rl_wsd_labeled.get_labeled_contexts(f)

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
