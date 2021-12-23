# gittish-build-schema

This project provides a common infrastructure for gittish projects providing
database schemas.

By strict convention, all database schemas must be authored with and be
deployed using SqlAlchemy/SqlAlchemy-Migrate alone.



## Build System Requirements 

Please note that these requirements only apply to the build process alone, most
of the artifacts will still be usable on different operating systems.

This project requires Debian Linux or a compatible derivate of it.

Other operating systems/derivates users will need to use a virtual machine of
some sort as we will not be supporting any other operating systems or derivates
any time soon. (read: provably never, use virtual machines or containers.)

And if you definitely need this to work natively on your operating system, feel
free to provide us with a feature request along with also a pull request.


## Setting up the Workspace

In order for this to work, you must create yourself a new folder that acts as
the `WORKSPACE_ROOT` for maintaining and building the various gittish projects,
e.g. 

```
> mkdir gittish
> cd gittish
```

Into that folder you will then clone the required gittish projects, e.g.

```
> git clone https://github.com/coldrye-gittish/gittish-build-schema.git
```

Have a look at the [build process configuration file](CONFIGURATION) wherein
the `GTS_DEPS` variable is defined. You have to clone all of the required
projects in order to make this work, e.g.

```
> . gittish-build-schema/CONFIGURATION && for dep in ${GTS_DEPS}; do \
git clone https://github.com/coldrye-gittish/${dep}.git ; \
done
```

It is important that you do not rename the original project folder names
as otherwise the configuration script will determine the wrong PACKAGE
and PROJECT name.


## Project Dependencies

The following gittish projects need to be available alongside this project.

* gittish-build-common
* gittish-build-python


## External Package Dependencies

In addition to the external package dependencies defined by the other gittish
projects, the following packages need to be installed.

* TBD


## Provided Makefiles

* [Makefile.standard.in](Makefile.standard.in)

Provides means to control the build lifecycle of a gittish schema project.


## Provided Templates

* [Standard Template](templates/standard)

The standard template is used to set up new gittish schema projects.


## Configuring the Build Process

In order to configure the overall build process, you must run the `configure`
script.

```
cd <WORKSPACE_ROOT>/gittish-build-schema
./configure
```

This will create the `CONFIG.in` file that is required by all the other projects.

This will take some time as the externals will be fetched and compiled.

