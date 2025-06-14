from selenium.webdriver.common.by import By


class MainFunctionalityLocators:

    CONSTRUCTOR = (By.CSS_SELECTOR, "header nav ul li:first-child a p")
    ORDER_FEED = (By.CSS_SELECTOR, "header nav ul li.ml-2 a p")
    INGREDIENT = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_WINDOW = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 h2")
    CROSS_BTN = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    FIELD_FOR_ADDING_INGREDIENTS = (By.CSS_SELECTOR, "div.constructor-element_pos_top")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "ul:nth-child(2) a:first-child div.counter_counter__ZNLkj p")
    CREATE_ORDER_BTN = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7 button")
    ORDER_FEED_WINDOW = (By.CSS_SELECTOR, "p.text.text_type_main-medium.mb-15")