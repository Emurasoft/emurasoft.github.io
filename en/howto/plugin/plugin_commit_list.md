# To Use CommitList Plug-in

TheCommitList plug-in is installed by default with EmEditor Professional. This plug-in shows the current changes and the commit history of a Git repo. To use theCommitList plug-in, click ![CommitList](../../images/plugin_commit_list.gif) on thePlug-ins bar. Or in theTools menu, point toPlug-ins, and then clickCommitList.

Some features of CommitList require Git to be installed and callable from command prompt with the command `git`.

## Changes sidebar

The plug-in will first check if the current document is in a[Git](https://git-scm.com/) repo. If it is, the repo will be opened and its repo status will be shown. You can click on theOpen... button in the sidebar to open a different repo.

Current changes and staged changes are shown in the sidebar. Staged changes are changes that were added to the index. All other changes to the working directory are shown in the changes list.

Right-clicking on a changed file in the sidebar will show a menu with commands for that changed file. You canStage orUnstage the change. You canUndo Changes to revert the file to the previous state. You can alsoView Changes andOpen File in the editor. Clicking onRefresh will refresh the changed files list.

CommitList monitors the file system so that if a file in the repo directory was modified by an external program, the sidebar is refreshed.

ThePull button pulls changes from the remote to the local repo.Push sends local changes to the remote repo. If the current branch is not associated with an upstream branch, the upstream branch will be created before pushing changes to it. These commands print a message to the status bar on completion.

ThePull andPush buttons may also display a number to indicate the number of commits behind or ahead of the upstream branch. "Pull (1)" means that there is 1 commit to pull and "Push (1)" means that there is 1 commit to push. TheAutofetch option in the menu is useful for updating these numbers periodically.

You can click on the> button to access more commands.

-Refresh refreshes the changed files list.

-Command Output shows the output of previous commands.

- TheStatus command prints the output of `git status`.

- TheFetch command updates your remote-tracking branches.

-Open Repo Folder opens the repo folder in File Explorer.

- If the current branch has an upstream branch,Open Repo Website opens the project's source control and collaboration website, like GitHub, in the web browser.

- IfAutofetch is enabled, `git fetch` is called every 3 minutes.

-Help opens this page.

You can change the current branch with the dropdown menu. Changing the branch is equivalent to the command `git checkout branch`. Conflicting changes will prevent you from checking out a branch.

The edit control below the branch dropdown is where you can write a commit message. Click onCommit Staged/Commit All to either commit the staged changes or to stage all changes and commit. The commit will be made to the currently selected branch.

## Commit list

Click on theCommit List button to view the commit history. When a commit is selected, the right panel displays the commit details and the list of files changed on this commit. Right-click on a file in the list and selectCompare with Previous to see what changed to the file on this commit.

In the commit list, you can right-click on a commit and selectCopy to copy the commit details.Browse Files At Commit will show the directory tree when the commit was made. AndCompare Commits will show you the differences between two commits.

You can checkout the commit withCheckout (--detach), which creates a detached HEAD. If you want to create a new branch from the commit, selectCreate New Branch....

You can filter the list by clicking onFilter History…. Enter theFilter String, select aFilter By option, then clickFilter. The commit list now only shows commits that match the filter. TheX button next to theFilter History… button cancels the filter.

The left panel shows a list of branches in the repo. SelectView Branch to show the list of commits for that branch. You canCheckout Branch to switch to the branch,Create New Branch from the selected branch, orDelete Branch. When two branches are selected, you can compare the files between those branches withCompare Branches.

If a file that is in the current repo is opened in the editor, theView History For Current Document button can be selected. It lists any commits that include changes to the current file. Right-clicking on a commit will show four options.Show Commit jumps to that commit in the main commit list.Compare with Previous compares the file with its previous revision.Compare File at Commits compares the file at two different commits.Compare with File in Working Tree compares the file at the selected commit and the work tree version.

## Tips

- Press theF6 key orESC key to set the keyboard focus back to the editor.
