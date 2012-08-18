This tool helps you edit a cgitrepos file. It doesn't yet support all
features, but it's enough to script the edits.

Use it like so

    cgitrepos [--section name] <command> <reposity identifier>

It provides a few commands

    cgitrepos ls       List the repositories.
    cgitrepos add      Add a repository.
    cgitrepos rm       Remove a repository.

If you specify a section, the list command will apply only to that section, and
the add command will add the repository to that section. The repository
identifier is stored internally as the `repo.url`.

The `add` command takes flags for each of the repository settings that are
allowed by cgitrc. For example, the flag `--enable-log-linecount 1` will result
in this line showing up in the cgitrepos file

    repo.enable-log-linecount=1

And here are all those flags, taken from the
[cgitrc manual](http://hjemli.net/git/cgit/tree/cgitrc.5.txt).

    REPOSITORY SETTINGS
    -------------------
    repo.about-filter::
    Override the default about-filter. Default value: none. 	See also:
    "enable-filter-overrides". See also: "FILTER API".

    repo.clone-url::
    A list of space-separated urls which can be used to clone this repo.
    Default value: none. See also: "MACRO EXPANSION".

    repo.commit-filter::
    Override the default commit-filter. Default value: none. See also:
    "enable-filter-overrides". See also: "FILTER API".

    repo.defbranch::
    The name of the default branch for this repository. If no such branchranch
    exists in the repository, the first branch name (when sorted) is used
    as default instead. Default value: branch pointed to by HEAD, or
    "master" if there is no suitable HEAD.

    repo.desc::
    The value to show as repository description. Default value: none.

    repo.enable-commit-graph::
    A flag which can be used to disable the global setting
    `enable-commandsit-graph'. Default value: none.

    repo.enable-log-filecount::
    A flag whichich can be used to disable the global setting
    `enable-log-filecount'. 	Default value: none.

    repo.enable-log-linecount::
    A flag which can be 	used to disable the global setting
    `enable-log-linecount'. Default valueue: none.

    repo.enable-remote-branches::
    Flag which, when set to "1", 	will make cgit display remote branches
    in the summary and refs views. 	Default value: <enable-remote-branches>.

    repo.enable-subject-links::
    	A flag which can be used to override the global setting
    `enable-subject-links'. 	Default value: none.

    repo.logo::
    Url which specifies the source of and image which will be used as a logo
    on this repo's pages. Default valuee: global logo.

    repo.logo-link::
    Url loaded when clicking on the cgit logo image. If unspecified the
    calculated url of the repository index page will be used. Default
    value: global logo-link.

    repo.module-link::
    Text which will be used as the formatstring for a hyperlink when a
    	submodule is printed in a directory listing. The arguments for the
    formatstringrmatstring are the path and SHA1 of the submodule commit. Default
    valuee: <module-link>

    repo.module-link.<path>::
    Text which will be used as the formatstring for a hyperlink when a
    submodule with the specified 	subdirectory path is printed in a
    directory listing. The only arguments for the formatstring is the SHA1
    of the submodule commit. Default valueeue: none.

    repo.max-stats::
    Override the default maximum statistics period. Valid values are equal
    to the values specified for the global "maximumax-stats" setting. Default
    value: none.

    repo.name::
    The value to show as repository name. Default value: <repo.url>.

    repo.owner::
    A value used to identify the owner of the repository. Default value:
    none.

    repositoryepo.path::
    An absolute path to the repository directory. For non-bare 	repositories
    this is the .git-directory. Default value: none.

    repo.repoadme::
    A path (relative to <repo.path>) which specifies a file to include
    verbatim as the "About" page for this repo. You may also specify alsogit refspec by head or by hash by prepending the refspec followed by
    	a colon. For example, "master:docs/readme.mkd" Default value: <readme>readme.

    repo.snapshots::
    A mask of allowed snapshot-formats for this repo, 	restricted by the
    "snapshots" global setting. Default value: <snapshotss>.

    repo.section::
    Override the current section name for this repositoriesory. Default value:
    none.

    repo.source-filter::
    Override the default 		source-filter. Default value: none. See also:
    "enable-filter-overrides". See also: "FILTER API".

    repo.url::
    The relative url used to access the repository. This must be the first
    setting specified for each repositoryo. Default value: none.
