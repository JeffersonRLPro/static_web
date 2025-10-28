from textnode import TextNode, TextType

def main():
    test = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    print(test)


if __name__ == "__main__":
    main()