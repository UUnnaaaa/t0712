import urllib.parse
import requests


def query_pchome(keyword: str):
    encoded_keyword = urllib.parse.quote(keyword)
    response = requests.get(
        f"https://ecshweb.pchome.com.tw/search/v4.3/all/results?q={encoded_keyword}&page=1&pageCount=40"
    )

    # https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=%E8%A1%8C%E5%8B%95%E9%9B%BB%E6%BA%90&page=1&pageCount=40
    data = [
        {
            "name": prod["Name"],
            "pricing": float(prod["Price"]),
        }
        for prod in response.json()["Prods"]
    ]
    return data

def query_eslite(keyword: str):
    encoded_keyword = urllib.parse.quote(keyword)
    response = requests.get(
        f"https://holmes.eslite.com/v1/search?q={encoded_keyword}&page_size=20&page_no=1&final_price=0,&sort=desc&branch_id=0"
    )

    # https://holmes.eslite.com/v1/search?q=+%E8%A1%8C%E5%8B%95%E9%9B%BB%E6%BA%90&page_size=20&page_no=1&final_price=0,&sort=desc&branch_id=0
    data = [
        {
            "name": result["name"],
            "pricing": float(result["final_price"]),
        }
        for result in response.json()["results"]
    ]
    return data


if __name__ == "__main__":
    print(query_eslite("行動電源"))
