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

Pipeline_Code_Generation = """
                          Your are expert in Writing the code for the following constraints. 
                          Focus on implementing the core functionality first, ensuring the code is optimized for memory efficiency, 
                          space constraints, and free from memory leaks. The code should prioritize functionality over test cases. 
                          Use best practices for embedded systems to manage memory and resources effectively. 
                          Generate the Code for the {task_description} in {language} eventhough user asks for the test_cases. 

                          """

Pipeline_Test_Case_Generation = """
                               
                              Generate comprehensive test cases for the embedded systems code that performs the following task:
                              {code}. The test cases should thoroughly verify all aspects of functionality, 
                              including normal operation, edge cases, and error handling. Additionally, 
                              ensure tests check for memory efficiency, confirm no memory leaks, 
                              and validate the code’s behavior under space-constrained conditions. 
                              Design the test cases to simulate real-world conditions and ensure the system’s reliability and stability.

                               """

Pipeline_Test_Case_Generation1 = """
                               
                              You are an expert in unit testing. Your task is to generate comprehensive test cases using Google Mock or 
                              CppUTest for the provided code. The test cases should cover various aspects such as functionality, edge cases, 
                              and error handling. Ensure that the test cases are detailed and include the following:
                              Generate a GoogleMock or CppUTest test cases for the {code}


                               """