import streamlit as st


def advanced():

    st.write(
        """
        
        Github options allow several advanced options to execute fine grained operations on workflow. This section
        covers some of the most important aspects
        
    """
    )
    st.write("")

    with st.expander("Context object"):
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

  