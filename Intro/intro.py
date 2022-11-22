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

        """
        )