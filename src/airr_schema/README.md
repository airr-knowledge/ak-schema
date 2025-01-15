# AIRR Standards schema for incorporation into AKC LinkML

We use git submodule to bring in multiple versions of the AIRR standards. The current
supported versions are:

* airr-standards-v1.5: release-1.5 branch
* airr-standards-v2.0: master branch

Both versions are currently checked out to a branch, versus a tag, as the AIRR standards
are still undergoing development. Once there is a stable tag then we can link to it
specifically instead of the branch.

Note that the submodule does not automatically follow the branch. Instead it is linked
to a specific commit, so new changes must be explicitly pulled and committed. For example,
to update v1.5 with any recent changes:

```
# pull latest
cd airr-standards-v1.5
git checkout release-1.5
git pull

# Now you can commit the directory like a typical file
cd ..
git add airr-standards-v1.5
git commit -m "update airr standards v1.5 with latest changes"
```

Also note that these submodules are essentially a `git clone` of the repository, so you
can create/switch branches, make/commit/push changes, etc., assuming that you have
privileges on the airr-standards repository.
