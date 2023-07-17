# Repo Information

This Repository contains notes and tooling around implementing coding standards on repositories as part of the data science clinic and related projects. This repository also contains a few scripts which analyze repositories and code using automation. 

Information on the specific tests and automation can be found in the scripts directory README file.

# Coding Standards for UChicago DSI

Motivation:
---
Much of the code that is produced here at the DSI is 80% complete and not in a state that it can be easily turned over. The purpose of this document is to provide a set of best practices _in checklist form_ so that we can quickly do code reviews and provide expectations on them.

We should always keep the following in mind: Analysis is _useless_ without a good repo.

Principles:
---
1. Automation
    -- All tasks should be automated
1. Reproducability
    -- All results should be reproducible
1. Documentation
    -- All tasks and results should be clearly documented
1. Data chain of ownership
    -- Data should have an obvious chain from source to result

Level 1: Bare minimum.
---
1. Docker / Dockerfile:
    * There should be a dockerfile and instructions on how to run the code in the main README file.
    * All code should be run via docker.
    * The Dockerfile should use a `requirements.txt` to manage modules and should have versions on all modules.
    * NOTE: in the case that the code is being run on the AI or DSI cluster, docker can be avoided.
1. Directory structure and naming should be obvious and easy to understand.
1. There should be no secrets or API Keys in the repo.
1. There should be no hard-coded paths.
1. File names should be useful:
    * There should be no ``v2`` or dates or people's name in filenames.
1. Notebooks should _not_ contain function definitions.
1. Notebooks should have less than 10 cells and all cells should be 15 lines of code or less.
1. Notebooks should have documentation (preferably markdown) which describes the purpose of them.
1. Function names should be descriptive.
1. Documentation should include (at a _minimum_):
    * Doc strings on all functions
    * README files in directories specifying the contents.
    * README file in the root directory describing the purpose of the code, where to look for things and how to run the code. If there are other locations for information regarding this project, links should be provided. 
1. `.gitignore` should be used to avoid committing data and intermediate data files which are not appropriate for the repo.
    * There should be no `DS_Store` files or `.ipynb_checkpoints` directories

1. Working branches need to be up do date with _main_ upon completion of task/code review and should not stray behind _main_ for more than day.

Level 2: Almost useful.
---
1. Proper use of github:
    * Branches should be merged into main _and then deleted_
    * There should be both a _dev_ and _main_ branch. Code should follow the following path:
        1. _working branch_ -> _dev_ -> _main_ where each is a PR.
1. Linting:
    * All code should pass basic linting

Level 3: Actually good practice.
---
1. Tests
    * Adding unit tests for all functions
1. Github actions
    * For linting and testing on DEV branch


FAQ
---

* How will testing of the above be done?

```On a code review day, the repo will be cloned, the dockfile built and the notebooks run. The notebooks will be inspected for the practices above. While the main branch will be the focus, each branch will be looked at to determine how far astray of main it is.```

* How do I handle output images or tables?

```Use an \output directory to put in images and other results```

* If I can't put functions in notebooks, where should they go? 

```Functions should be put in a utils directory and loaded via import```

* How should I document notebooks?

```Notebooks should be well-documented.  Does the notebook begin with a title, byline, date, and summary/description? Is its content logically organized into sections with headers? Does it walk the viewer through what the code is doing and why using both Markdown and comments, and in clear language?```

```Notebooks should be readable. Has cell output been formatted for easier viewing (e.g., to avoid scrolling)? Are there any cells that were obviously used for testing/scratchwork and have not yet been removed? Are Python module imports located together near the top of the notebook, in accordance with PEP 8, rather than scattered throughout many cells? Are all cells 15 lines of code or less?  Are numbers rounded for display purposes?```

* What about Docker README.md information?

This is a great start, where project-name is the project name you are working on. 

```Docker Information

This repository contains a basic dockerfile that will run a jupyter notebook instance. To build the docker image, please type in:

docker build . -t [project-name]

Note that the image name in the above command is drw

To run the image type in the following:

docker run -p 8888:8888 -v ${PWD}:/tmp [project-name]

as you can see we are running the [project-name] image.
```

There is also a dockerfile that has been used in the past.

* What is a good folder structure?

```For the simplest projects something like the below should work: 

.
├── README.md
├── .gitignore
├── Dockerfile
├── notebooks/
│   ├── README.md
│   └── notebook Files
├── utils/
│   ├── README.md
│   ├── __init__.py
│   └── python utility files
├── data/
│   ├── README.md (or SOURCES.md)
│   └── Data files
├── output/
│   ├── README.md
│   └── output images, tables, etc.
└── documentation/
    └── README.md
```
