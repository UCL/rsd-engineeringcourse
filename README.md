# rsd-engineeringcourse

Course materials for Research Software Engineering course.


## Content:

In this course, you will move beyond programming, to learn how to construct reliable, readable, efficient research software in a collaborative environment. The emphasis is on practical techniques, tips, and technologies to effectively build and maintain complex code. This is a semester module (30 hours over 10 half-days), intensive, practical course. The content of each of the 10 half-day units is as follows:

1. Code management. Distributed version control. Git. Github
1. Collaborating around code. Issue tracking. Code review and pull requests. Branches and merging
1. Introduction to Python and Scientific programming
1. Analysing and plotting Research data 
1. Testing scientific software. Unit testing, regression testing. Test-driven design. Expectations and assertions. Mocking. Build-and-test servers. Negative testing. Sensible error messages. Setting up Continuous Integration.
1. Documenting software projects. Managed logging. Debugging and debuggers. Coverage measurement. Finding errors in the past.
1. Writing libraries and creating packages. Software licenses. Citing software. Software sustainability. Comments. Coding conventions. 
1. Software as engineering. Pragmatic use of diagram languages. Requirements engineering. Agile and Waterfall. Functional and architectural design.
1. Best practice in construction. Design and development. Object-oriented design. 
1. Analysing performance. Profiling code. Developing faster code.

## Prerequisites:

- You must have reasonable experience in at least one compiled language, such as C++, C, or Fortran, and at least one dynamic language, such as Python, Ruby, Matlab or R.
- You must also have experience of the Unix shell.

Examples and exercises for this course will be provided in Python.  You will therefore find it easiest to follow along if you have experience in it. Appropriate Python experience could be obtained from the Software Carpentry workshops. Previous experience with version control (such as from Software Carpentry) would be helpful.

You are required to bring your own laptop to the course as the classrooms we are using do not have desktop computers.

# Contributing to this repository

This repository contains the course notes as jupyter notebooks. This makes it a bit difficult to contribute and to review contributions. Please, only include changes in the cells modified and not other metadata that changes when running them.

⚠ Do not run `make` locally on your computer! ⚠ 

It will produce side effects on your global git configuration!
Instead, follow the instructions below.

## Testing it locally

The site is built using gh-actions. If you'd like to test the actions locally,
you can run the actions using [`act`](https://github.com/nektos/act) command
tool. By default this will run the action in a copy of the repository and you
won't be able to inspect the steps that happened. If you'd like to keep the
output in the current directory, use the `-b` (bind) flag.

```bash
$ act -b
[Build website/Build-website] 🚀  Start image=catthehacker/ubuntu:act-latest
[Build website/Build-website]   🐳  docker run image=catthehacker/ubuntu:act-latest platform= entrypoint=["/usr/bin/tail" "-f" "/dev/null"] cmd=[]
[Build website/Build-website] ⭐  Run actions/checkout@v2
[Build website/Build-website]   ✅  Success - actions/checkout@v2
[Build website/Build-website] ⭐  Run actions/cache@v2
INFO[0000]   ☁  git clone 'https://github.com/actions/cache' # ref=v2 
[Build website/Build-website]   ✅  Success - actions/cache@v2
[Build website/Build-website] ⭐  Run Install TeXLive
INFO[0000]   ☁  git clone 'https://github.com/DanySK/setup-texlive-action' # ref=0.1.1 
[Build website/Build-website]   ✅  Success - Install TeXLive
[Build website/Build-website] ⭐  Run Setup Python
INFO[0001]   ☁  git clone 'https://github.com/actions/setup-python' # ref=v2 
[Build website/Build-website]   ✅  Success - Setup Python
[Build website/Build-website] ⭐  Run Install dependencies
INFO[0001]   ☁  git clone 'https://github.com/py-actions/py-dependency-install' # ref=v2 
[Build website/Build-website]   ✅  Success - Install dependencies
[Build website/Build-website] ⭐  Run Building notes
[Build website/Build-website]   ✅  Success - Building notes
[Build website/Build-website] ⭐  Run Builds website
INFO[0001]   ☁  git clone 'https://github.com/helaili/jekyll-action' # ref=v2 
[Build website/Build-website]   🐳  docker run image=act-helaili-jekyll-action-v2:latest platform= entrypoint=[] cmd=[]
[Build website/Build-website]   ✅  Success - Builds website
```

Alternatively, if you want to only run the jekyll build step once you've run the whole action, you can use the official jekyll containers with:

```bash
$ docker run --rm --volume="$PWD:/srv/jekyll" --volume="$PWD/vendor/bundle:/usr/local/bundle" -p 4000:4000 -it jekyll/jekyll:latest jekyll serve
```

and open http://localhost:4000/rsd-engineeringcourse (or the link provided).
Note that this is mounting the `bundle` directory where `act` will create them.
