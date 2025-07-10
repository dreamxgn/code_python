import requests

def main():
    response = requests.get("https://www.baidu.com")
    print(response.status_code)
    print(response.text[:100])

if __name__ == "__main__":
    main()
