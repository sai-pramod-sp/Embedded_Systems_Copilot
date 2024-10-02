Generation = """
            Generate a {language} code sample for an embedded system. 
            The code should perform the following task: {task_description} without having any memory leaks, less time complexity,
            space complexity.

            """

Optimization = """
            You are an expert in optimizing code for performance, memory usage, and readability. 
            You will receive a piece of code and your task is to provide an optimized version of it. 
            Ensure that the optimized code maintains the same functionality as the original.
            Here is the code that needs optimization in {language} language:
            {task_description}
            Please provide an optimized version of the code, focusing on improving performance, 
            reducing memory usage, and enhancing readability

            """

Test_Case_Generation = """
                You are an expert in {language} unit testing. Your task is to generate comprehensive test cases using Google Mock or 
                CppUTest for the provided {task_description} code. The test cases should cover various aspects such as functionality, edge cases, 
                and error handling. Ensure that the test cases are detailed and include the following:
                Generate a GoogleMock or CppUTest test cases for the {language} provided with the {task_description}

                """