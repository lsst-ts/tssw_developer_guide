.. _GitHub_Workflows:

GitHub Workflows
================

We have a limited amount of free usage of GitHub Actions, but we are currently well under that
limit. Small GitHub Actions are fine to add, but longer jobs may need discussion or approval.

Use of GitHub Workflows (Actions) in SSW projects is not required, but there are a few
suggested tools. The suggested tools are collected into the repository at
https://github.com/lsst-ts/tssw_workflows. It contains the following:

* ``enforce_rebase`` checks that the branch is rebased onto the latest ``develop`` branch.

  .. literalinclude:: ./enforce_rebase.yaml
     :language: yaml
     :caption: .github/workflows/enforce_rebase.yaml

* ``lint`` uses the standard pre-commit configuration and runs ``generate_pre_commit_conf`` and all
  pre-commit hooks.

  .. literalinclude:: ./lint.yaml
     :language: yaml
     :caption: .github/workflows/lint.yaml

* ``news_creation`` confirms that at least one news fragment has been added.

  .. literalinclude:: ./news_creation.yaml
     :language: yaml
     :caption: .github/workflows/news_creation.yaml

Although the ``lint`` action is redundant with Jenkins, the other two provide independent checks;
however, the addition of the ``lint`` action gives rapid feedback when lint rules have been violated
and makes the information available to users who don't have access to Jenkins.
