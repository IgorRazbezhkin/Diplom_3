from selenium.webdriver.common.by import By


class OrderFeedSectionLocators:

    ORDER = (By.CSS_SELECTOR, "ul li:first-child a div.OrderHistory_textBox__3lgbs p.text_type_digits-default")
    ORDER_DETAILS_WINDOW = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 div.Modal_modal__container__Wo2l_")
    ORDER_ID_WINDOW = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq")
    COMPLETED_ALL_TIME = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")
    COMPLETED_TODAY = (By.CSS_SELECTOR, "div:nth-child(3) p.OrderFeed_number__2MbrQ")
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")
    ORDER_ID_HISTORY = (By.CSS_SELECTOR, "ul li:first-child a div.OrderHistory_textBox__3lgbs p.text_type_digits-default")
    ID_LAST_ORDER = (By.CSS_SELECTOR, "ul li:first-child a div.OrderHistory_textBox__3lgbs p.text_type_digits-default")

