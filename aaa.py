from abc import ABC, abstractmethod


class MenuItem:
    def __init__(self):
        self.itemId = 0
        self.displayName = ""
        self.sumOfRating = 0
        self.numberOfPeopleWhoRatedIt = 0


class IMenuRecommendation(ABC):
    @abstractmethod
    def addItem(self, id, displayName):
        pass

    @abstractmethod
    def getRecommendedItem(self):
        pass

    @abstractmethod
    def outOfStockItem(self, itemId):
        pass

    @abstractmethod
    def restockItem(self, itemId):
        pass

    @abstractmethod
    def makeDealOfTheDayItem(self, itemId):
        pass

    @abstractmethod
    def rateItem(self, itemId, rating):
        pass


class MenuRecommendation(IMenuRecommendation):
    def __init__(self):
        self.menu_items = {}
        self.in_stock = set()
        self.deal_of_the_day = None

    def addItem(self, id, displayName):
        menu_item = MenuItem()
        menu_item.itemId = id
        menu_item.displayName = displayName
        menu_item.sumOfRating = 0
        menu_item.numberOfPeopleWhoRatedIt = 0

        self.menu_items[id] = menu_item
        self.in_stock.add(id)

    def getRecommendedItem(self):
        if not self.menu_items:
            return None

        if self.deal_of_the_day is not None and self.deal_of_the_day in self.in_stock:
            return self.menu_items[self.deal_of_the_day]

        highest_rating = -1
        recommended_item = None

        for item_id in self.in_stock:
            item = self.menu_items[item_id]
            average_rating = 0
            if item.numberOfPeopleWhoRatedIt > 0:
                average_rating = item.sumOfRating / item.numberOfPeopleWhoRatedIt

            if (average_rating > highest_rating or
                    (average_rating == highest_rating and
                     (recommended_item is None or item.itemId < recommended_item.itemId))):
                highest_rating = average_rating
                recommended_item = item

        return recommended_item

    def outOfStockItem(self, itemId):
        if itemId in self.in_stock:
            self.in_stock.remove(itemId)

        if self.deal_of_the_day == itemId:
            self.deal_of_the_day = None

    def restockItem(self, itemId):
        if itemId in self.menu_items:
            self.in_stock.add(itemId)

    def makeDealOfTheDayItem(self, itemId):
        if itemId in self.menu_items and itemId in self.in_stock:
            self.deal_of_the_day = itemId

    def rateItem(self, itemId, rating):
        if itemId in self.menu_items:
            item = self.menu_items[itemId]
            item.sumOfRating += rating
            item.numberOfPeopleWhoRatedIt += 1


if __name__ == "__main__":
    total_number_of_requests = int(input().strip())
    menu_recommendation = MenuRecommendation()

    for request_number in range(1, total_number_of_requests + 1):
        arr = input().strip().split(" ")
        command = arr[0]

        if command == "addItem":
            item_id = int(arr[1])
            display_name = arr[2]
            menu_recommendation.addItem(item_id, display_name)
        elif command == "getRecommendedItem":
            menu_item = menu_recommendation.getRecommendedItem()
            if menu_item is None:
                print("N/A")
            else:
                average_rating = (
                    0 if menu_item.numberOfPeopleWhoRatedIt == 0 else menu_item.sumOfRating / menu_item.numberOfPeopleWhoRatedIt
                )
                print(f"{menu_item.itemId} {menu_item.displayName} Rating: {average_rating}")
        elif command == "outOfStockItem":
            item_id = int(arr[1])
            menu_recommendation.outOfStockItem(item_id)
        elif command == "restockItem":
            item_id = int(arr[1])
            menu_recommendation.restockItem(item_id)
        elif command == "makeDealOfTheDayItem":
            item_id = int(arr[1])
            menu_recommendation.makeDealOfTheDayItem(item_id)
        elif command == "rateItem":
            item_id = int(arr[1])
            rating = int(arr[2])
            menu_recommendation.rateItem(item_id, rating)