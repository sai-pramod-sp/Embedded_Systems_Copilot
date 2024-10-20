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
                Generate a GoogleMock or CppUTest test cases for the {language} language provided with the {task_description}

                """

Text_Generation = """
                Please provide a detailed explanation about {task_description} in the context of embedded systems. 
                Ensure the response is informative and does not include any code. Focus on explaining the concepts, 
                applications, and significance of the topic.

                  """

Pipeline_Test_Case_Generation = """
                                Generate the code for the following task in the context of embedded systems: {task_description}. 
                                The outcome should contain all the requirements, constraints, functionalities with memory management, space management 
                                in the form of Code. Ensure the code is optimized for performance and memory usage in {language} language. 
                                The system is built to Prioritize generating the core code that accomplishes the task first. If the user asks for test cases, 
                                provide them only after completing the task implementation and ensuring the embedded system's core functionality

                                """