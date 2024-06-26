forest_dict = {
    'Бой': """
                        ||Так как это первый бой, тут будет объяснено все на пальцах.                 ||
                        ||Сперва ты выбираешь как ходить (Атака/Дальняя атака/Способность)            ||
                        ||Затем бросается двадцатигранный кубик,                                      ||
                        ||если выпавшее число больше брони противника,то бросается второй             ||
                        ||куб на урон.Бой закончится когда один из дуэлянтов падет.                   ||
                        ||В случае выигранной битвы ты можешь обыскать труп и может быть              ||
                        ||тебе повезет на какой-нибудь скраб,удачи!                                   ||
                        """,
    'Лес': {
        'id_location': 1,
        'description': """
                        ||Лес густой и тенистый, с высокими деревьями, закрывающими небо.              ||
                        ||Воздух влажный и тяжелый, пахнет прелой листвой и грибами.                   ||
                        ||Птицы щебечут в ветвях, а насекомые стрекочут в траве.                       ||
                        ||Лес кажется мирным и спокойным, но вы чувствуете,                            ||
                        ||что за этой тишиной скрывается опасность.                                    ||
                        ||Внезапно вы слышите шорох в кустах.                                          ||
                        """,
    },
    'После_боя': {
        'id_location': 1.1,
        'description': """
                        ||Отряхнувшись и выдохнув ты начинаешь осматриваться,остерегаясь,             ||
                        ||что гоблин был не один.Но все что нарушало естественную тишину              ||
                        ||это постукивание дятла на дереве                                            ||
                        ||и все тот же теплый ветер.                                                  ||
                        ||Подойдя к кусту, откуда выпрыгнул гоблин ты                                 ||
                        ||увидел хорошо замаскированную землянку...                                   ||
                        """,
        'action': {
            '|В землянку|': '|Вы пытаетесь спустится посмотреть,что там внутри|',
            '|Уйти|': '|Вы продолжаете свой путь глубже в лес|'

        }

    },
    'Землянка': {
        'id_location': 2,
        'description': """
                        ||Гоблинская землянка - это небольшое, грязное строение,                       ||
                        ||построенное из веток, грязи и соломы.                                        ||
                        ||Она низкая и узкая, с единственной дверью и без окон.                        ||
                        ||Внутри землянки темно и душно. Воздух пахнет дымом,                          ||
                        ||едой и немытыми телами. Землянка                                             ||
                        ||заполнена беспорядочно разбросанными вещами - одеждой, едой и т.д.           ||
                        ||В центре землянки находится странное углубление в камне.                     ||
                        ||Углубление круглое и гладкое, и кажется, что оно было сделано искусственно.  ||
                        ||Гоблины не знают, что это за углубление, но они считают его священным.       ||
                        ||Они используют его для проведения своих ритуалов и церемоний.                ||
                        ||Говорят, что углубление обладает магическими свойствами.                     ||
                        ||Некоторые гоблины утверждают,что они слышали голоса,исходящие из углубления. ||
                        ||Другие говорят, что они видели, как из углубления выходило странное свечение.||
                        ||Правда ли это или нет, неизвестно. Но гоблины верят в магию углубления,      ||
                        ||и они относятся к нему с почтением и страхом.                                ||
                        """,
        'action': {
            '|Уйти|': '|Вы спешно покидаете эту нору|',
            '|Взаимодействие|': """|Вы пытаетесь вставить медальон поднятый ранее с гоблина,вокруг вас в 
            радиусе 3х метров вспыхивает фиолетовое пламя, на том месте,куда вы положили медальон ,
            теперь стоит маленький алтарь, резкий голос в голове,тяжелый,каменный голос говорит тебе:
             - для получения доступа к сокровищу ,отдайте плоть|
            """

        }

    },
    'Поселение': {
        'id_location': 3,
        'description': """
                        ||Пробираясь глубже в лес, ты натыкаешься на поляну, залитую мягким            ||
                        ||лунным светом.Посреди поляны стоит изящное дерево с серебристыми листьями.   ||
                        ||Вдруг ты слышишь мелодичный звук флейты. Музыка льется чистым и нежным       ||
                        ||потоком, наполняя лес гармонией.Ты идешь к дереву и видишь фигуру,           ||
                        ||сидящую под ним. Это эльф, облаченный в одежды изумрудного цвета.            ||
                        ||Его волосы длинные и струящиеся, а глаза полны мудрости и спокойствия.       ||
                        ||Эльф приветствует тебя кивком головы и жестом приглашает сесть рядом с ним.  ||
                       """,
        'action': {
          '|Cесть|':'|Кивнуть в ответ и присесть рядом|',
          '|Уйти|' :'|Эльфов слушать- себя не уважать,пройти мимо|',
          '|TheOnlyThingTheyFearIsYou|': '|Ты молча достаешь меч,и заставляешь его замолчать|'
        }
    },
    'Ворота': {
        'id_location': 4.2,
        'description': """
                        ||За поселением эльфов, в самом сердце леса, находятся огромные, исполинские   ||
                        ||древние ворота. Ворота сделаны из черного металла и покрыты ржавчиной        ||
                        ||и пылью веков. Они настолько высоки, что их вершины теряются                 ||
                        ||в листве деревьев.Дверь в воротах разрушена, и через нее можно пройти.       ||
                        ||За дверью виднеется длинный, темный туннель, ведущий в неизвестность.        ||
                        ||Говорят, что эти ворота ведут в кузни богов, где некогда выплавлялись        ||
                        ||легендарные клинки. Клинки, выкованные в этих кузнях, обладали невероятной   || 
                        ||силой и остротой.Но кузни богов давно заброшены, и никто не знает,           ||
                        ||что случилось с теми, кто там работал. Некоторые говорят, что боги           ||
                        ||покинули кузни, разочаровавшись в смертных. Другие говорят, что кузни        ||
                        ||были разрушены во время великой войны между богами и демонами.Правда ли это  ||
                        ||или нет, неизвестно. Но ворота в кузни богов по-прежнему стоят, как          ||
                        ||напоминание о славном прошлом и о том, что даже самые могущественные         ||
                        ||создания могут пасть.                                                        ||
                        ||Тихий голос в голове нашёптывает .."прочти"...."что именно тебе непонятно"...||
                        ||Странно.
                       """,
        'action': {
            '|Попытаться осмотреться|': '|Можно попытаться осмотреться и понять,чего хочет голос|',
            '|Скорей-быстрей|': '|Какой голос, вы видите что за ворота,пусть дальше ищет дураков,я иду дальше|'
        },
    },
    'Комната_награда': {
        'id_location': 4.3,
        'description': """
                        ||Наградна комната - это небольшое помещение, вырезанное в скале. Комната слабо||
                        ||освещена факелами, отбрасывающими мерцающие тени на стены.В центре комнаты   ||
                        ||стоит стол, на котором разложены различные предметы. Это награды, которые    ||
                        ||эльф обещал тебе за выполнение его задания.                                  ||
        """

    },
    'Болота': {
        'id_location': 4.1,
        'description': """
                        ||Болота простираются за поселением эльфов, как бескрайнее море грязи и воды.  ||
                        ||Воздух тяжелый и влажный, пахнет гнилью и разложением.Вода в болотах мутная  ||
                        ||и коричневая, и в ней плавают всевозможные мерзкие существа. Пиявки          ||
                        ||прикрепляются к любой обнаженной коже, а комары роятся вокруг, жаждущие крови||
                        ||По болотам можно передвигаться только по узким тропинкам, которые вьются     ||
                        ||между кочками и ямами. Тропинки скользкие и опасные, и легко оступиться и    ||
                        ||упасть в трясину.В болотах обитают всевозможные опасные существа, такие как  ||
                        ||гигантские змеи, ядовитые пауки и плотоядные растения. Существа эти хорошо   ||
                        ||замаскированы в болотной растительности, и на них легко наткнуться.Но болота ||
                        ||также являются домом для редких и ценных трав и растений. Травники часто 
                        ||рискуют своей жизнью, чтобы собрать эти растения, которые можно использовать ||
                        ||для создания мощных зелий и лекарств.Болота - это опасное, но и красивое     ||
                        ||место. Это место, где жизнь и смерть идут рука об руку, и где можно найти    ||
                        ||как великие сокровища, так и ужасные опасности.Находясь в середине           ||
                        ||локации вы видите как постепенно дорога разделяется...
                      """,
        'action': {
          '|Проход к заброшенному храму|':'|Надо закончить задание,которое мне дал эльф|',
          '|Проход к исполните желаний|':'|Вы видите за холмом молнии,которые хаотично бьют в землю,иду смотреть|'
        },
    },
    'Заброшенный_Храм': {
        'id_location': 5.1,
        'description':"""
                       ||Проход к заброшенному храму с болот скрыт в густом тумане, который постоянно  ||
                       ||висит над болотами. Чтобы найти проход, нужно следовать за слабым свечением,  ||
                       ||которое исходит из глубины тумана.Свечение приведет вас к узкой тропинке,     ||
                       ||которая вьется между кочками и ямами. Тропинка скользкая и опасная, и легко   ||
                       ||оступиться и упасть в трясину.По мере того,как вы будете следовать по тропинке||
                       ||туман будет становиться все гуще, а звуки болота будут затихать. Вы будете    ||
                       ||чувствовать себя все более и более изолированным и одиноким.В конце концов, вы||
                       ||доберетесь до заброшенного храма. Храм стоит на небольшом островке посреди    ||
                       ||болота. Он выглядит древним и запущенным, но вы чувствуете, что внутри него   ||
                       ||скрывается что-то ценное.
                       ||Заброшенный храм изнутри выглядит так же мрачно и удручающе, как и снаружи.   ||
                       ||Стены покрыты трещинами и паутиной, а пол усеян осколками стекла и камней.    ||
                       ||Воздух тяжелый и затхлый, и в нем витает запах плесени и разложения.          ||
                       ||Единственным источником света являются слабые лучи солнца, проникающие через  ||
                       ||трещины в стенах.В центре храма находится большой алтарь, на котором стоит    ||
                       ||статуя божества. Статуя покрыта пылью и паутиной, и ее черты стерлись от      ||
                       ||времени.Справа от алтаря находится проход, ведущий в святилище. Святилище -   ||
                       ||это небольшая комната, в центре которой находится трон. На троне сидит босс,  ||
                       ||которого вам нужно убить.
                       ||Когда вы входите в святилище, босс начинает насмехаться над вами.             ||
                       ||-“Итак, ты пришел, чтобы убить меня?” - говорит он.                           ||
                       ||-“Ты жалкий смертный. У тебя нет ни единого шанса победить меня.”             ||
                       """,
        'action':{
            "|Ответ|(Приведет к началу боя)":"|Я пришел сюда по заданию эльфа. Ты должен быть уничтожен.|",
            '|Уйти|':'|Он слишком большой,а эльф вряд-ли даст что-то стоящее|'

},
    },
    'Исполнитель': {
        'id_location': 5.2,
        'description':"""
                       """
    }
}