import streamlit as st


def intro():

    st.write(
        """
        
        Github offers repository related automation services called github actions.
        These allow users to perform various automated tasks associated with the
        code repository management and CI/ CD pipelines. Github actions consists off:

        * Workflows: (Attached to repository, contain jobs, triggerd upon events)
        * Jobs: (define execution environments, contain steps, can be conditional)
        * Steps: (execute shell script commands, can use third party actions, can be conditional)

        Workflows can be defined for each repository under the tab actions. Workflows are defined with the yml files 
        and stored under .github/workflows. Repositories can have several workflows.

        [Extensive official documentation]('https://docs.github.com/en/actions')
        
    """
    )
    st.write("")

    with st.expander("Document Structure"):
        st.write(
            """
            Workflow yml document has several levels which are defined with reserved keywords.

            * name : (name of the workflow)
            * on: (manually or automatically trigger events)
            * jobs: (jobs to execute)
            * runs-on: (defines the running enviromnent. | enables running multiple commands)
            * steps: (list of steps to execute)
            * uses: (call defined github action)
            * with: (takes keywords to additionally configure the action)

        """
        )

    with st.expander("Triggers & Events"):
        st.write(
            """
            Github offers the following repository related events:

            * push : (pushing commits)
            * pull_request: (pull_request | opened or closed)
            * create (a branch or tag was created)
            * fork (repository was forked)
            * issues (issue opened or deleted)
            * issue_comment (issue or pull request comment action)
            * watch (repository was stared)
            * discussion (discussion action)

            And repository non-related events:

            * workflow_dispatch: manually trigger workflow
            * repository_dispatch: REST API request triggers workflow
            * schedule: workflow schedule
            * workflow_call: called by other workflows

            [Official Documentation](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)


        """
        )
