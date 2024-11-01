from llama3 import BedrockLLaMA as bd

class MyOtherClass:
    def __init__(self):
        self.llama_model = bd()  # This should work if the class is defined correctly

    def generate_text(self, input_text):
        return self.llama_model._call(input_text)

if __name__ == "__main__":
    my_class = MyOtherClass()
    result = my_class.generate_text("Translate this text to English.")
    print(result)