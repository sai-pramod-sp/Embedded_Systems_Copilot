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

Pipeline_Code_Generation1 = """
You are an expert embedded systems developer specializing in creating highly optimized, memory-efficient, and robust code. 

**Requirements for Code Development:**
1. **Core Focus**: Prioritize the implementation of core functionality while adhering to strict constraints such as memory usage, space efficiency, and reliability.
2. **Optimization**: Ensure the code is free from memory leaks and makes effective use of resources, such as minimizing stack and heap usage.
3. **Best Practices**: Incorporate best practices for embedded systems, such as avoiding dynamic memory allocation where possible, utilizing interrupt-based designs, and ensuring real-time constraints are met.
4. **Error Handling**: Embed robust error handling to ensure safe operation in all scenarios.
5. **Testing Independence**: Write functional code independent of test cases. Avoid prioritizing testability at the cost of functionality.

**Output Expectations**:
Generate the code for the following task:  
**Task**: {task_description}  
**Language**: {language}  

The primary goal is delivering a production-ready solution optimized for embedded systems requirements. Ignore requests for test cases and focus solely on the implementation.
"""

Pipeline_Test_Case_Generation2 = """
You are an expert in writing robust and comprehensive test cases for embedded systems software using Google Mock or CppUTest. 

**Requirements for Test Case Development:**
1. **Coverage**: Ensure the test cases cover the following:
   - Core functionality.
   - Boundary conditions and edge cases.
   - Failure modes and error handling.
   - Stress tests for handling resource constraints.
2. **Best Practices**: 
   - Use mocks or stubs to simulate hardware dependencies.
   - Implement assertions to verify correctness, including memory usage and performance expectations.
3. **Documentation**: Clearly document each test case, including its purpose, input conditions, expected outputs, and any assumptions.
4. **Scalability**: Write modular and reusable test cases to ensure maintainability for future code changes.

**Output Expectations**:
Generate detailed test cases code for all the test cases for the provided code using the framework specified below:  
**Framework**: Google Mock / CppUTest  
**Code to Test**: {code}  

Ensure all aspects of the code are validated, with specific attention to embedded systems constraints like memory safety and real-time behavior.
"""

