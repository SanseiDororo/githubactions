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
            Contexts are objects which store information about the workflow. Specific segments of the workflow
            as for example environment variables or secrets can be used for the specific operations.

            Attributes of the context are stored in the

            ```
            ${{github}}
            
            Human friendly output

            ${{toJSON(github)}}
    
            ```


            [Official Documentation Page]('https://docs.github.com/en/actions/learn-github-actions/contexts')

        """
        )

    with st.expander("Execution Control"):
        st.write(
            """
            Github actions provide several keywords to control execution of the jobs.

            1. Conditions.

            If we want to execute jobs under specific conditions, we can use if keyword.
            
            ```
            - name: Upload tests
                if: failure() && steps.id_of_the_step.outcome == 'failure'
                uses: actions/upload-artifact@v3
                with: 
                    name: create-report
                    path:test.py

            ```
            Additional Example:
            
             ```
            - name: Use cached
                if: steps.cache.outputs.cache-hit != 'true'
                run: |
                    pip install pipenv
                    pipenv install black

            ```


            [Control Flow Official Documentation]('https://docs.github.com/en/actions/learn-github-actions/expressions')
        """
        )

  