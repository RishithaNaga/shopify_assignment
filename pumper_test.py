from pythonProject.pageObjects.home_page import Home_page


homepage_obj=Home_page()
homepage_obj.navigate_to_shopify_partners()
homepage_obj.navigate_to_shopify_partners()
homepage_obj.click_become_a_partner_button()
homepage_obj.click_login_on_create_account_shopping_popup()
homepage_obj.login_to_shopify_to_continue_with_partners('nagarishitha181292@gmail.com', 'Shopify@123')
homepage_obj.click_logged_in_user_on_welcome_popup()
homepage_obj.click_login_to_store_button_and_switch_to_new_window()
homepage_obj.click_choose_account_link()
homepage_obj.click_apps_button()
homepage_obj.click_pumper_bundle_search_result_link()
homepage_obj.switch_to_app_iframe()
homepage_obj.click_create_offer_button()
homepage_obj.click_create_a_quantity_break_button()
homepage_obj.click_select_a_product_button()
homepage_obj.add_product_to_offer()
homepage_obj.apply_offer_template_then_publish()
homepage_obj.click_products_from_navigation()
homepage_obj.click_preview_online()
homepage_obj.verify_offer_on_product_page()





