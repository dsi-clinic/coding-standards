# There are 3 structures required for a quarter:
# XXX_YEAR_PROJECT: This is a list of lists
#   items should be:
#        1. name
#        2. url
#        3. mentor
#        4. TA
#        5. github location
#        6. flag 1/0 for if repo is private or not
#        7. if there is a one-pager 1/0
#        8. External Mentor Info
#        9. if the URL (item 2) can pass the github link test

# XXX_YEAR_STUDENT is a list of lists
#   items should be:
#        1. Project (matches to the project in PROJECT)
#        2. Student Name (what appears on the webpage)
#        3. github url OR just the github user name (if the text does not
#                begins with https:// then "https://github.com/" will be added

# XXX_YEAR_NAME_MAP
# This is an override for the name. It replaces what is used internally with
# something readable. It is a dictionary with the name link to the new name


AUTUMN_23_PROJECT = [
    [
        "AmFam",
        "https://www.amfam.com/",
        "Anna",
        "Eddie",
        "https://github.com/dsi-clinic/2023-autumn-amfam",
        1,
        0,
        "<ul><li>Tim Rouse</li><li>Jessie Zhu</li></ul>",
        1,
    ],
    [
        "Argonne",
        "https://www.anl.gov/",
        "Bill Trok & YJ Choe",
        "Yu-Wei Chen",
        "https://github.com/dsi-clinic/2023-clinic-Argonne",
        1,
        1,
        "[Matthew Dearing](https://scholar.google.com/citations?user=HUQIELDxZkgJ&hl=en)",
        1,
    ],
    [
        "Argonne-Fermi",
        "https://www.anl.gov/",
        "Isaac",
        "Jessica J",
        "https://github.com/dsi-clinic/2023-autumn-argonne-fermi",
        1,
        1,
        "[Matthew Dearing](https://scholar.google.com/citations?user=HUQIELDxZkgJ&hl=en)",
        1,
    ],
    [
        "Climate Cabinet",
        "https://climatecabinet.org/",
        "Trevor",
        "Avery",
        "https://github.com/dsi-clinic/2023-fall-clinic-climate-cabinet",
        0,
        1,
        "Caleb Braun",
        1,
    ],
    [
        "CPL",
        "https://www.chipublib.org/",
        "Tim",
        "Yiran",
        "https://github.com/dsi-clinic/2023-autumn-cpl",
        1,
        1,
        "Abigail Sullivan",
        1,
    ],
    [
        "Fermi-simulations",
        "https://computing.fnal.gov/kevin-pedro/",
        "Rituparno Mandal & Peter",
        "Eddie",
        "https://github.com/dsi-clinic/2023-Autumn-Clinic-Fermi-CaloDiffusionPaper",
        0,
        1,
        "<ul><li>Oz Amram</li><li>Kevin Pedro</li></ul>",
        1,
    ],
    [
        "Fermi-gnn",
        "https://computing.fnal.gov/giuseppe-cerati/",
        "Chong Liu",
        "Jessica J",
        "https://github.com/exatrkx/NuGraph",
        0,
        1,
        "Giuseppe Cerati",
        1,
    ],
    [
        "HAPA",
        "https://www.hapahi.org/",
        "Rahim & Trevor",
        "Victor",
        "https://github.com/dsi-clinic/2023-fall-clinic-hawaii-pesticides",
        1,
        1,
        "<ul><li>Fern Ānuenue Holland</li><li>Anne Frederick</li><li>Emily Marquez</li></ul>",
        1,
    ],
    [
        "Internet Equity",
        "https://internetequity.uchicago.edu/",
        "Tim & Jonatas Marques",
        "Soham",
        "https://github.com/dsi-clinic/2023-autumn-internet-equity",
        1,
        1,
        "Alexis Schrubbe",
        1,
    ],
    [
        "IRC",
        "https://www.rescue.org/",
        "Rahim",
        "Avery",
        "https://github.com/dsi-clinic/2023-autumn-irc",
        1,
        1,
        "Atish Gonsalves",
        1,
    ],
    [
        "Morningstar",
        "https://www.morningstar.com/",
        "Patricia & David U.",
        "Soham",
        "https://github.com/dsi-clinic/2023-autumn-morningstar",
        1,
        0,
        "<ul><li>Josh Charney</li><li>Jazmin Melchor</li></ul>",
        1,
    ],
    [
        "Perpetual",
        "https://www.perpetualuse.org/",
        "Rahim",
        "Yiran",
        "https://github.com/dsi-clinic/2023-clinic-perpetual",
        1,
        1,
        "Ellie Moss",
        1,
    ],
    [
        "Prudential",
        "https://www.prudential.com/",
        "Nick",
        "Sunvid",
        None,
        1,
        0,
        "<ul><li>Jyoti Singh</li><li>Dr. Mitchell Stern</li><li>Gavin Smith</li><li>William Liang</li><li>Leo Shen</li></ul>",
        1,
    ],
    [
        "RAFI",
        "https://www.rafiusa.org/",
        "Todd & Chris",
        "Sunvid",
        "https://github.com/uchicago-dsi/rafi-poultry",
        0,
        1,
        "Aaron Johnson",
        0,
    ],
    [
        "UNI",
        "https://coe.uni.edu/curriculum-instruction/directory/taraneh-matloob-haghanikar-phd",
        "Satadisha Saha Bhowmick",
        "Victor",
        "https://github.com/dsi-clinic/2023-autumn-matloob-lab",
        1,
        1,
        "Taraneh Matloob",
        1,
    ],
]

AUTUMN_23_STUDENT = [
    ["AmFam", "DB Christenson", "https://github.com/dbchristenson"],
    ["AmFam", "Grace Wang", "https://github.com/graceannwang"],
    ["AmFam", "Jennifer Yeaton", "https://github.com/jkyeaton"],
    ["AmFam", "Leon (Lixin) Wang", "https://github.com/leonwlx"],
    ["Argonne", "Yushu Qiu", "https://github.com/yushuqiu1"],
    ["Argonne", "Jason Yu", "https://github.com/JasonYUChicago"],
    ["Argonne", "Mayurakshi Ghosal", "https://github.com/m-ghosal"],
    ["Argonne", "Yingzi Jin", "https://github.com/jinyz1220"],
    ["Argonne-Fermi", "Nicholas Liagridonis", "https://github.com/niclia"],
    ["Argonne-Fermi", "Foo Suon Chuang", "https://github.com/foosuonchuang"],
    [
        "Argonne-Fermi",
        "Yuanning (Violet) Huang",
        "https://github.com/yuanninghuang",
    ],
    ["Argonne-Fermi", "Zihua Chen", "https://github.com/zihua-uc"],
    ["Climate Cabinet", "Alan Mburu Kagiri", "https://github.com/alankagiri"],
    ["Climate Cabinet", "Aïcha Camara", "https://github.com/necabotheking"],
    ["Climate Cabinet", "Nicolas Posner", "https://github.com/nrposner"],
    ["Climate Cabinet", "Yuzhou Wang", "https://github.com/yuzhouw313"],
    ["CPL", "Anika Vyas", "https://github.com/anikavyas"],
    ["CPL", "Jeremy Dumalig", "https://github.com/jeremydumalig"],
    ["CPL", "Matthew Rubenstein", "https://github.com/Rubemat20"],
    ["CPL", "Kristof Turan", "https://github.com/kris057"],
    [
        "Fermi-simulations",
        "Keegan Ballantyne",
        "https://github.com/kmballantyne",
    ],
    ["Fermi-simulations", "Carina Kane", "https://github.com/carinakane"],
    ["Fermi-simulations", "Douglas Williams", "https://github.com/Douglasmsw"],
    ["Fermi-gnn", "Jihee You", "https://github.com/jiheeyy"],
    ["Fermi-gnn", "Rohan Mehta", "https://github.com/rohanmehtagithub"],
    ["Fermi-gnn", "Kate Habich", "https://github.com/ehabich"],
    ["Fermi-gnn", "Shan Gao", "https://github.com/shaangao"],
    ["HAPA", "Yangge Xu", "https://github.com/ygxu01"],
    ["HAPA", "Chen Hui Wang (Fei)", "https://github.com/chenhuifei01"],
    ["HAPA", "Jonathan Juarez", "https://github.com/Nohakith"],
    ["HAPA", "Sam Corey", "https://github.com/secorey"],
    ["Internet Equity", "Ridhi Purohit", "https://github.com/ridhi96"],
    ["Internet Equity", "Neha Sadasivan", "https://github.com/nehasadasivan"],
    ["Internet Equity", "Angelie Miranda", "https://github.com/aemiranda"],
    ["Internet Equity", "Aaron Haefner", "https://github.com/aaronhaefner"],
    ["IRC", "Helen Zhou", "https://github.com/helenyxzhou"],
    ["IRC", "Annabel Mendoza", "https://github.com/amendoza5025"],
    ["IRC", "Santiago Segovia", "https://github.com/ssegovba"],
    ["Morningstar", "Rohan Mathur", "https://github.com/rmathur1482"],
    ["Morningstar", "Kaya Lee", "https://github.com/klee2024"],
    ["Morningstar", "Rishabh Shastry", "https://github.com/rishabhshastry"],
    ["Morningstar", "Jihui Tan", "https://github.com/JihuiTanUchicago"],
    ["Perpetual", "Jessica Cibrian", "https://github.com/jescib"],
    ["Perpetual", "Huanlin Dai", "https://github.com/HuanlinDai"],
    ["Perpetual", "Sarah Walker", "https://github.com/sarahwalker10"],
    ["Perpetual", "Yifan Wu", "https://github.com/genieugod"],
    ["Prudential", "Sirivanth Paladugu", "https://github.com/Sirivanth16"],
    ["Prudential", "Connie Chen", "https://github.com/kangyic"],
    ["Prudential", "Jiayan Li", "https://github.com/jiayanaddsalt"],
    ["Prudential", "Qichang Zheng", "https://github.com/QichangZheng"],
    ["RAFI", "Colin McLuckie", "https://github.com/ColinMcLuckie"],
    ["RAFI", "Shishira Bhavimane", "https://github.com/sbhavimane-22"],
    ["RAFI", "Fanghan Xu", "https://github.com/catalystxu"],
    ["RAFI", "Yutong Jiang", "https://github.com/essicaJ"],
    ["UNI", "Su Doga Karaca", "https://github.com/sudogakrc"],
    ["UNI", "Maxine Ling Xu", "https://github.com/mxu2000"],
    ["UNI", "Anna Moise", "https://github.com/amoise16"],
    ["UNI", "Hantao Xiao", "https://github.com/hantaoxiao"],
]

AUTUMN_23_NAME_MAP = {
    "UNI": "Taraneh Matloob Literature Lab",
    "HAPA": "Hawaii Alliance for Progressive Action",
    "IRC": "International Rescue Committee",
    "CPL": "Chicago Public Library",
    "Fermi-simulations": "Fermilab Simulations",
    "Fermi-gnn": "Fermilab Graph Neural Networks",
}

WINTER_23_NAME_MAP = {"PCDC": "Pediatric Cancer Data Commons"}

WINTER_23_PROJECT = [
    [
        "Argonne",
        "https://www.anl.gov/",
        "Rahim & Trevor",
        None,
        "https://github.com/dsi-clinic/2023-clinic-Argonne",
        1,
        1,
        "[Matthew Dearing](https://scholar.google.com/citations?user=HUQIELDxZkgJ&hl=en)",
        1,
    ],
    [
        "BankTrack",
        "https://www.banktrack.org/",
        "Trevor & Patricia",
        None,
        "https://github.com/chicago-cdac/banktrack-loan-pipeline/",
        1,
        1,
        "<ul><li>Ryan Brightwell</li><li>Dustin Roasa</li></ul>",
        1,
    ],
    [
        "Blue Ocean Gear",
        "https://www.blueoceangear.com/",
        "Trevor",
        "Todd",
        "https://github.com/chicago-cdac/bog-anomaly-mapping",
        1,
        1,
        "<ul><li>Kortney Opshaug</li><li>Peter Macy</li><li>Will Morton</li></ul>",
        1,
    ],
    [
        "BPI",
        "https://www.impactforequity.org/",
        "Riley",
        "Kenia",
        "https://github.com/dsi-clinic/2022-bpi-clinic",
        1,
        1,
        "<ul><li>Amy Thompson</li><li>Loren Jones</li></ul>",
        1,
    ],
    [
        "DRW",
        "https://drw.com/",
        "Nick",
        None,
        "https://github.com/dsi-clinic/2023-clinic-drw",
        1,
        0,
        "Ian Adam",
        1,
    ],
    [
        "Fermi",
        "https://computing.fnal.gov/michael-kirby/",
        "Peter",
        "Todd",
        "https://github.com/dsi-clinic/2023-clinic-fermi-tag",
        1,
        1,
        "<ul><li>Michael Kirby</li><li>Meghna Bhattacharya</li></ul>",
        1,
    ],
    [
        "First Republic Bank",
        "https://www.firstrepublic.com/",
        "Nick",
        None,
        "https://github.com/dsi-clinic/2023-clinic-first-republic-bank",
        1,
        0,
        '<ul><li>Chris Csiszar</li><li>Mark Woodworth</li></ul>',
        1,
    ],
    [
        "GreenWave",
        "https://www.greenwave.org/",
        "Trevor",
        None,
        "https://github.com/dsi-clinic/2023-clinic-greenwave",
        1,
        1,
        "Kendall Barbery",
        1,
    ],
    [
        "Invenergy",
        "https://invenergy.com/",
        "Anna",
        "UT",
        "https://github.com/dsi-clinic/2022-Invenergy-clinic",
        1,
        0,
        "<ul><li>Zoë Kimpel</li><li>Kenneth Parkhill</li></ul>",
        1,
    ],
    [
        "Morningstar",
        "https://www.morningstar.com/",
        "David U. & Patricia",
        "UT",
        "https://github.com/dsi-clinic/2023-clinic-morningstar",
        1,
        0,
        "<ul><li>Josh Charney</li><li>Jazmin Melchor</li></ul>",
        1,
    ],
    [
        "PCDC",
        "https://commons.cri.uchicago.edu/pcdc/",
        "Tim",
        None,
        "https://github.com/chicago-cdac/2023-clinic-pcdc",
        1,
        1,
        "Michael Watkins",
        1,
    ],
    [
        "Perpetual",
        "https://www.perpetualuse.org/",
        "Rahim",
        None,
        "https://github.com/dsi-clinic/2023-clinic-perpetual",
        0,
        1,
        "Ellie Moss",
        1,
    ],
    [
        "Prudential",
        "https://www.prudential.com/",
        "Nick",
        None,
        None,
        1,
        0,
        "Amol Tembe",
        1,
    ],
    [
        "RISC",
        "https://risc.uchicago.edu/",
        "Jeffrey",
        "Anthony",
        "https://github.com/dsi-clinic/2023-clinic-risc",
        1,
        1,
        "Noah Duncan",
        1,
    ],
    [
        "Neurocritical Care",
        "https://profiles.uchicago.edu/profiles/display/17338286",
        "Yuetian",
        "Anthony",
        "https://github.com/dsi-clinic/2023-clinic-neurocritical-care",
        1,
        1,
        "Dr. Ali Mansour",
        1,
    ],
    [
        "Internet Equity",
        "https://internetequity.uchicago.edu/",
        "James Turk",
        "Kenia",
        "https://github.com/chicago-cdac/broadbandequity",
        1,
        1,
        "Nicole Marwell",
        1,
    ],
]

WINTER_23_STUDENT = [
    ["Argonne", "Soren Dunn", "https://github.com/sorendunn"],
    ["Argonne", "Richard Huang", "https://github.com/rrhuang"],
    ["Argonne", "Grace Shao", "https://github.com/graceshaoy"],
    ["BankTrack", "Nivedita Vatsa", "https://github.com/nivedita-k-vatsa"],
    ["BankTrack", "Yifu Hou", "https://github.com/yifu-hou"],
    ["BankTrack", "Grishma Bhattarai", "https://github.com/grishmab"],
    ["BankTrack", "Gillian Major", "https://github.com/gillianmajor"],
    ["Blue Ocean Gear", "Gautam Kapoor", "https://github.com/grkapoor17"],
    ["Blue Ocean Gear", "Ming-Chieh Liu", "https://github.com/ming-chieh-liu"],
    ["Blue Ocean Gear", "Henry herzog", "https://github.com/hgherzog"],
    ["BPI", "Ashley Hitchings", "https://github.com/ashleyhitchings"],
    ["BPI", "Justin Kim", "https://github.com/jykim21"],
    ["BPI", "Akila Forde", "https://github.com/aforde17"],
    ["DRW", "Mahnoor Khan", "https://github.com/Mfk-han"],
    ["DRW", "Xin Li", "https://github.com/xin2006"],
    ["DRW", "Jasmeet Singh Sandhu", "https://github.com/jasmeeetSingh"],
    ["DRW", "Yulun Han", "https://github.com/YLHan97"],
    ["Fermi", "Richard Zhang", None],
    ["Fermi", "Yuxin Ji", "https://github.com/Yuxin-Ji"],
    ["Fermi", "Jason Zhang", "https://github.com/Zhang-QC"],
    ["First Republic Bank", "Zhiyun Hu", "https://github.com/zhiyun0707"],
    ["First Republic Bank", "Guangbo Niu", "https://github.com/ngbdsb"],
    ["First Republic Bank", "Yu-Hsuan Chou", "https://github.com/yhchou0904"],
    ["First Republic Bank", "Ning Tang", "https://github.com/tangn121"],
    ["GreenWave", "Cole von Glahn", "https://github.com/cvg117"],
    ["GreenWave", "Piper Kurtz", "https://github.com/kurtzpuc"],
    ["GreenWave", "Nico Vila Alarcon", "https://github.com/niicovila"],
    ["Invenergy", "David Bukowski", "https://github.com/dtbukowski"],
    ["Invenergy", "Daisuke Kageyama", "https://github.com/daisukekageyama"],
    ["Invenergy", "Baichen Tan", "https://github.com/BaichenTan"],
    ["Invenergy", "Suyash Lakhani", "https://github.com/"],
    ["Morningstar", "Emily Yeh", "https://github.com/Emily-fyeh"],
    ["Morningstar", "Ruiquan Chang", "https://github.com/rqchang"],
    [
        "Morningstar",
        "Pedro Antonio Ramonetti Vega",
        "https://github.com/PRAMONETTI",
    ],
    ["Morningstar", "Nicole Li", "https://github.com/linicoley"],
    ["PCDC", "Xuerong Shang", "https://github.com/xuerong98"],
    ["PCDC", "Yu Zhou (Zoey)", "https://github.com/zoeyzhou1296"],
    ["PCDC", "Shuhan Liu", "https://github.com/ShannaLiu"],
    ["Perpetual", "Izzy Allum", "https://github.com/iallum"],
    ["Perpetual", "Ziyu Ren", "https://github.com/AshleyZR"],
    ["Perpetual", "Sandra Mauro", "https://github.com/sandramauro"],
    ["Perpetual", "Yushu Qiu", "https://github.com/yushuqiu1"],
    ["Prudential", "Yujing Sun", "https://github.com/yujing-syj"],
    ["Prudential", "Cole Silva", "https://github.com/silva-cole"],
    ["Prudential", "Nayna Pashilkar", "https://github.com/npashilkar"],
    ["RISC", "Carolyn Liu", "https://github.com/Crliu4"],
    ["RISC", "Avery Schoen", "https://github.com/averyschoen"],
    ["RISC", "Adil Kassim", "https://github.com/adilkassim"],
    [
        "Neurocritical Care",
        "Alexander Przybycin",
        "https://github.com/AlexPrizzy",
    ],
    [
        "Neurocritical Care",
        "Oishee Chakrabarti",
        "https://github.com/chakraoishee",
    ],
    [
        "Neurocritical Care",
        "Zachary Rothstein",
        "https://github.com/Zacharyr41",
    ],
    ["Neurocritical Care", "Jim Tinley", "https://github.com/jtinley0"],
    ["Internet Equity", "Maia Boyd", "https://github.com/maiaboyd"],
    ["Internet Equity", "Victoria Kielb", "https://github.com/vkielb"],
    ["Internet Equity", "Kaya Borlase", "https://github.com/borlasekn"],
    ["Internet Equity", "Brendon Krall", "https://github.com/bkrall36"],
]


SPRING_23_PROJECT = [
    [
        "Argonne",
        "https://www.anl.gov/",
        "Rahim",
        "Christian",
        "https://github.com/dsi-clinic/2023-clinic-Argonne",
        1,
        1,
        "[Matthew Dearing](https://scholar.google.com/citations?user=HUQIELDxZkgJ&hl=en)",
        1,
    ],
    [
        "Blue Ocean Gear",
        "https://www.blueoceangear.com/",
        "Launa",
        None,
        "https://github.com/chicago-cdac/bog-anomaly-mapping/",
        1,
        1,
        "<ul><li>Kortney Opshaug</li><li>Peter Macy</li><li>Will Morton</li></ul>",
        1,
    ],
    [
        "CRI-SET",
        "https://pediatrics.uchicago.edu/research/set",
        "Anna & Dan N.",
        "Anthony K",
        "https://github.com/dsi-clinic/2023-spring-clinic-set",
        1,
        1,
        "Dr. Henry David",
        1,
    ],
    [
        "DRW",
        "https://drw.com/",
        "Tim",
        None,
        "https://github.com/dsi-clinic/2023-clinic-drw",
        1,
        0,
        "Ian Adam",
        1,
    ],
    [
        "Fermi",
        "https://computing.fnal.gov/michael-kirby/",
        "Peter",
        "Ali",
        "https://github.com/dsi-clinic/2023-clinic-fermi-tag",
        1,
        1,
        "<ul><li>Michael Kirby</li><li>Meghna Bhattacharya</li></ul>",
        1,
    ],
    [
        "FRB",
        "https://www.firstrepublic.com/",
        "Nick",
        None,
        "https://github.com/dsi-clinic/2023-clinic-first-republic-bank",
        1,
        0,
        "<ul><li>Chris Csiszar</li><li>Mark Woodworth</li></ul>",
        1,
    ],
    [
        "Hawaii",
        "https://tsffoundation.org/",
        "Launa",
        "Ali",
        "https://github.com/chicago-cdac/hawaii-pesticides",
        1,
        1,
        "<ul><li>Fern Ānuenue Holland</li><li>Anne Frederick</li><li>Emily Marquez</li></ul>",
        0,
    ],
    [
        "IE",
        "https://internetequity.uchicago.edu/",
        "James Turk",
        "Kenia",
        "https://github.com/chicago-cdac/broadbandequity",
        0,
        1,
        "Dr. Nicole Marwell",
        1,
    ],
    [
        "Morningstar",
        "https://www.morningstar.com/",
        "Patricia & David U.",
        "Christian",
        "https://github.com/dsi-clinic/2023-clinic-morningstar",
        1,
        0,
        "<ul><li>Josh Charney</li><li>Jazmin Melchor</li></ul>",
        1,
    ],
    [
        "Neurocritical Care",
        "https://scholar.google.com/citations?user=cs_tgvwAAAAJ&hl=en",
        "Yuetian",
        "Anthony",
        "https://github.com/dsi-clinic/2023-clinic-neurocritical-care",
        1,
        1,
        "Dr. Ali Mansour",
        1,
    ],
    [
        "Perpetual",
        "https://www.perpetualuse.org/",
        "Rahim",
        None,
        "https://github.com/dsi-clinic/2023-clinic-perpetual",
        0,
        1,
        "Ellie Moss",
        1,
    ],
    [
        "Prudential",
        "https://www.prudential.com/",
        "Nick",
        "Kenia",
        None,
        1,
        0,
        "Dave Powers",
        1,
    ],
]

SPRING_23_STUDENT = [
    ["Argonne", "Ken Kliesner", "https://github.com/kenkliesner"],
    ["Argonne", "Annabel Mendoza", "https://github.com/amendoza5025"],
    ["Argonne", "Kekun Han", "https://github.com/KekunH"],
    ["Blue Ocean Gear", "Gautam Kapoor", "https://github.com/grkapoor17"],
    ["Blue Ocean Gear", "Henry Herzog", "https://github.com/Hgherzog"],
    ["Blue Ocean Gear", "Irsa Ashraf", "https://github.com/irsa-ashraf"],
    ["Blue Ocean Gear", "Katy Barone", "https://github.com/kbarone"],
    ["CRI-SET", "Varun Mohan", "https://github.com/vmohan96"],
    ["CRI-SET", "Jun Tan", "https://github.com/JunTan2022"],
    ["CRI-SET", "Katherine Miao", "https://github.com/Katherine-Miao"],
    ["DRW", "Mahnoor Khan", "https://github.com/Mfk-han"],
    ["DRW", "Jasmeet Singh Sandhu", "https://github.com/jasmeeetSingh"],
    ["DRW", "Yulun Han", "https://github.com/YLHan97"],
    ["Fermi", "Richard Zhang", None],
    ["Fermi", "Manuel Martinez", "https://github.com/manmartgarc"],
    ["Fermi", "Mingyan Wang", "https://github.com/wmingyan"],
    ["Fermi", "Tarun Arora", "https://github.com/tarun2k"],
    ["FRB", "Guangbo Niu", "https://github.com/ngbdsb"],
    ["FRB", "Zhiyun Hu", "https://github.com/zhiyun0707"],
    ["FRB", "Yu-Hsuan Chou", "https://github.com/yhchou0904"],
    ["FRB", "Ning Tang", "https://github.com/tangn121"],
    ["Hawaii", "Ashley Hitchings", "https://github.com/ashleyhitchings"],
    ["Hawaii", "Qingyi He", "https://github.com/cindyheqy"],
    ["Hawaii", "Caleb Costa", "https://github.com/calebcosta1"],
    ["IE", "Victoria Kielb", "https://github.com/vkielb"],
    ["IE", "Chandler Hall", "https://github.com/cgwhall"],
    ["IE", "Sarah Lueling", "https://github.com/slueling"],
    ["Morningstar", "Rishabh Shastry", "https://github.com/rishabhshastry"],
    ["Morningstar", "Dhairya Karna", "https://github.com/DhairyaKarna"],
    ["Morningstar", "Max de Saint-Exupery", "https://github.com/MaxSaint01"],
    ["Neurocritical Care", "Soren Dunn", "https://github.com/sorendunn"],
    ["Neurocritical Care", "Alex Przybycin", "https://github.com/AlexPrizzy"],
    [
        "Neurocritical Care",
        "Prashant Kumar",
        "https://github.com/Prashant-Kumar700",
    ],
    ["Perpetual", "Ziyu Ren", "https://github.com/AshleyZR"],
    ["Perpetual", "Yushu Qiu", "https://github.com/yushuqiu1"],
    ["Perpetual", "Avery Schoen", "https://github.com/averyschoen"],
    ["Perpetual", "Ekansh Trivedi", "https://github.com/ekanshtrivedi"],
    ["Prudential", "Sunvid Aneja", "https://github.com/sunvidaneja"],
    ["Prudential", "Peihan Gao", "https://github.com/peihan12"],
    ["Prudential", "Sai Omkar Kandukuri", "https://github.com/S-Omkar-K"],
    ["Prudential", "Hantang Qin", "https://github.com/jenniferqinnn"],
]

SPRING_23_NAME_MAP = {
    "Argonne": "Argonne Knowledge Graph",
    "Fermi": "Fermi: Kirby Lab",
    "Hawaii": " Hawaii Alliance for Progressive Action",
    "IE": "Internet Equity",
    "FRB": "First Republic Bank",
}

AUTUMN_22_PROJECT = [
    [
        "AmFam",
        "https://www.amfam.com/",
        "Tim & Rahim & Yuetian",
        "Anthony K",
        "https://github.com/chicago-cdac/2022-amfam-clinic/",
        1,
        0,
        "",
        1,
    ],
    [
        "BankTrack",
        "",
        "Launa",
        "Anthony K",
        "",
        1,
        0,
        "",
        0,
    ],    
    [
        "Blue Ocean Gear",
        "https://www.blueoceangear.com/",
        "Launa & Susanna",
        "Todd",
        "",
        1,
        0,
        "",
        1,
    ],
    [
        "BPI",
        "https://www.impactforequity.org/",
        "Amanda",
        "Kenia",
        "https://github.com/dsi-clinic/2022-bpi-clinic",
        1,
        0,
        "",
        1,
    ],
    [
        "Citizen Data",
        "",
        "Jeffrey & Riley",
        "Todd",
        "https://github.com/dsi-clinic/2022-citizendata-clinic",
        1,
        0,
        "",
        0,
    ],
    [
        "Internet Equity",
        "https://github.com/uchicago-dsi/broadbandequity",
        "Nick & Evelyn",
        "Utkarsh",
        "https://github.com/uchicago-dsi/broadbandequity",
        0,
        0,
        "",
        1,
    ],
    [
        "Invenergy",
        "https://invenergy.com/",
        "Anna & Trevor & Peter",
        "Utkarsh",
        "https://github.com/dsi-clinic/2022-Invenergy-clinic",
        1,
        0,
        "",
        1,
    ],
    [
        "mBio",
        "",
        "Trevor & Patricia",
        "Kenia",
        "https://github.com/uchicago-dsi/mBio",
        1,
        0,
        "",
        0,
    ],
    [
        "Prudential",
        "https://www.prudential.com/",
        "Nick",
        "Utkarsh",
        "",
        1,
        0,
        "",
        1,
    ],
]

AUTUMN_22_STUDENT = [
    ['AmFam', 'Ruiquan Chang', 'rqchang'] ,
    ['AmFam', 'Yulun Han', 'YLHan97'] ,
    ['AmFam', 'Yuhan Sun', 'yuhan0616'] ,
    ['AmFam', 'Serena Huang', 'SerenaGongHuang'] ,
    ['BankTrack', 'Yutai Li', 'yutaili'] ,
    ['BankTrack', 'Xin Tang', 'XTang685'] ,
    ['BankTrack', 'Jiawei Xie', 'jiaweix22'] ,
    ['BankTrack', 'Cesar Anzola', 'cesaranzola945'] ,
    ['BankTrack', 'Grishma Bhattarai', 'grishmab'] ,
    ['Blue Ocean Gear', 'Hazel Chui', 'hazelchc'] ,
    ['Blue Ocean Gear', 'Jiyi Peng', 'AuroraPeng'] ,
    ['Blue Ocean Gear', 'Jieyu Jiao ', 'zoeyjiao1104'] ,
    ['Blue Ocean Gear', 'Brinda Sapra', 'brinda1410'] ,
    ['BPI', 'Gabrielle Meyers', 'gmeyers405'] ,
    ['BPI', 'Vincent Liu', 'jcvincentliu'] ,
    ['BPI', 'Yu-Hsuan Chou', ''] ,
    ['BPI', 'Emily Yeh', 'Emily-fyeh'] ,
    ['BPI', 'Justin Kim', 'jykim21'] ,
    ['Citizen Data', 'Gabriel Nicholson', 'Gabenicholson'] ,
    ['Citizen Data', 'Nicholas Simon', 'nicksimon7524'] ,
    ['Citizen Data', 'Jason Jia', 'jasonjiajs'] ,
    ['Citizen Data', 'Michael Wagner', 'wagnerlmichael'] ,
    ['Invenergy', 'Kaveri Chhikara', 'kaveriC'] ,
    ['Invenergy', 'Sophie Logan', 'sophielogan'] ,
    ['Invenergy', 'David Bukowski', 'dtbukowski'] ,
    ['Invenergy', 'Piper Kurtz', 'kurtzpuc'] ,
    ['mBio', 'Xinyu He', 'Victoriaxinyu'] ,
    ['mBio', 'Yuchen Zhou', 'yuchenzhou286'] ,
    ['mBio', 'Shuyuan Wang', 'shuyuan-lily'] ,
    ['mBio', 'Baotong Zhang', 'BaotongZh'] ,
    ['Prudential', 'Cole Silva', 'silva-cole'] ,
    ['Prudential', 'Daniel Gold', 'danielisaacgold'] ,
    ['Prudential', 'Oishee Chakrabarti', 'chakraoishee'] ,
    ['Prudential', 'Yujing Sun', 'yujing-syj'] ,
    ['Prudential', 'Gillian Major', 'gillianmajor'] ,
    ['Internet Equity', 'Sam Pavlekovsky', 'spavlekovsky'] ,
    ['Internet Equity', 'Kamran Ahmed', 'kamranahmed08'] ,
    ['Internet Equity', 'Maia Boyd', ''] ,
    ['Internet Equity', 'Bruno Xie', 'brunoxie'] ,
    ['Internet Equity', 'Kaya Borlase', 'borlasekn'] ,
    ['Internet Equity', 'Christelle Inema', 'ChristelleInema'] ,
]

AUTUMN_22_NAME_MAP = {}
