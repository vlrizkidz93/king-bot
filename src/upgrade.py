from .custom_driver import client
from .slot import find_slot
from .utils import log


def upgrade_slot(browser: client, id: int):
    el = find_slot(browser, id)
    el = el.find_element_by_xpath(".//div[contains(@class, 'clickable')]")
    browser.click(el, 1)
    browser.click(el, 1)

    log("added slot: {} to queue".format(id))