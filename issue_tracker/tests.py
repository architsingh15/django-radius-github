"""This the test that runs when we provide the run_selenium_test command"""
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""The test data that needs to be run on the application"""
test_data = [
    'https://github.com/mojombo/grit',
    'https://github.com/wycats/merb-core',
    'https://github.com/rubinius/rubinius',
    'https://github.com/mojombo/god',
    'https://github.com/vanpelt/jsawesome',
    'https://github.com/wycats/jspec',
    'https://github.com/defunkt/exception_logger',
    'https://github.com/defunkt/ambition',
    'https://github.com/technoweenie/restful-authentication',
    'https://github.com/technoweenie/attachment_fu',
    'https://github.com/Caged/microsis',
    'https://github.com/anotherjesse/s3',
    'https://github.com/anotherjesse/taboo',
    'https://github.com/anotherjesse/foxtracs',
    'https://github.com/anotherjesse/fotomatic',
    'https://github.com/mojombo/glowstick',
    'https://github.com/defunkt/starling',
    'https://github.com/wycats/merb-more',
    'https://github.com/macournoyer/thin',
    'https://github.com/jamesgolick/resource_controller',
    'https://github.com/jamesgolick/markaby',
    'https://github.com/jamesgolick/enum_field',
    'https://github.com/defunkt/subtlety',
    'https://github.com/defunkt/zippy',
    'https://github.com/defunkt/cache_fu',
    'https://github.com/KirinDave/phosphor',
    'https://github.com/bmizerany/sinatra',
    'https://github.com/jnewland/gsa-prototype',
    'https://github.com/technoweenie/duplikate',
    'https://github.com/jnewland/lazy_record',
    'https://github.com/jnewland/gsa-feeds',
    'https://github.com/jnewland/votigoto',
    'https://github.com/defunkt/mofo',
    'https://github.com/jnewland/xhtmlize',
    'https://github.com/ruby-git/ruby-git',
    'https://github.com/ezmobius/bmhsearch',
    'https://github.com/uggedal/mofo',
    'https://github.com/mmower/simply_versioned',
    'https://github.com/abhay/gchart',
    'https://github.com/benburkert/schemr',
    'https://github.com/abhay/calais',
    'https://github.com/mojombo/chronic',
    'https://github.com/sr/git-wiki',
    'https://github.com/queso/signal-wiki',
    'https://github.com/drnic/ruby-on-rails-tmbundle',
    'https://github.com/danwrong/low-pro-for-jquery',
    'https://github.com/wayneeseguin/merb-core',
    'https://github.com/sr/dst',
    'https://github.com/mojombo/yaws',
    'https://github.com/KirinDave/yaws',
    'https://github.com/sr/tasks',
    'https://github.com/mattetti/ruby-on-rails-tmbundle',
    'https://github.com/grempe/amazon-ec2',
    'https://github.com/wayneeseguin/merblogger',
    'https://github.com/wayneeseguin/merbtastic',
    'https://github.com/wayneeseguin/alogr',
    'https://github.com/wayneeseguin/autozest',
    'https://github.com/wayneeseguin/rnginx',
    'https://github.com/wayneeseguin/sequel',
    'https://github.com/bmizerany/simply_versioned',
    'https://github.com/peterc/switchpipe',
    'https://github.com/hornbeck/arc',
    'https://github.com/up_the_irons/ebay4r',
    'https://github.com/wycats/merb-plugins',
    'https://github.com/up_the_irons/ram',
    'https://github.com/defunkt/ambitious_activeldap',
    'https://github.com/atmos/fitter_happier',
    'https://github.com/brosner/oebfare',
    'https://github.com/up_the_irons/credit_card_tools',
    'https://github.com/jnicklas/rorem',
    'https://github.com/cristibalan/braid',
    'https://github.com/jnicklas/uploadcolumn',
    'https://github.com/simonjefford/ruby-on-rails-tmbundle',
    'https://github.com/chneukirchen/rack-mirror',
    'https://github.com/chneukirchen/coset-mirror',
    'https://github.com/drnic/javascript-unittest-tmbundle',
    'https://github.com/engineyard/eycap',
    'https://github.com/chneukirchen/gitsum',
    'https://github.com/wayneeseguin/sequel-model',
    'https://github.com/kevinclark/god',
    'https://github.com/hornbeck/blerb-core',
    'https://github.com/brosner/django-mptt',
    'https://github.com/technomancy/bus-scheme',
    'https://github.com/Caged/javascript-bits',
    'https://github.com/Caged/groomlake',
    'https://github.com/sevenwire/forgery',
    'https://github.com/technicalpickles/ambitious-sphinx',
    'https://github.com/lazyatom/soup',
    'https://github.com/josh/rails',
    'https://github.com/cdcarter/backpacking',
    'https://github.com/jnewland/capsize',
    'https://github.com/bs/starling',
    'https://github.com/sr/ape',
    'https://github.com/collectiveidea/awesomeness',
    'https://github.com/collectiveidea/audited',
    'https://github.com/collectiveidea/acts_as_geocodable',
    'https://github.com/collectiveidea/acts_as_money',
    'https://github.com/collectiveidea/calendar_builder',
    'https://github.com/collectiveidea/clear_empty_attributes',
    'https://github.com/collectiveidea/css_naked_day'
                ]

private_test_data = [
    'https://github.com/architsingh15/aruba_dashboard',
    'https://github.com/architsingh15/hiway-web',
    'https://github.com/architsingh15/anthe',
    'https://github.com/architsingh15/fiduciary-ai',
    'https://github.com/architsingh15/hiway-web-migrate',
    'https://github.com/architsingh15/hiway',
    'https://github.com/architsingh15/rdbtools-web',
    'https://github.com/architsingh15/rdbtools-app'
]
# get path from settings.py


def automated_test():
    # Selenium web driver for opening the browser and running the automation tests
    browser = webdriver.Chrome(
        executable_path='/home/hasher/Desktop/django-radius-github/issue_tracker/drivers/chromedriver'
    )

    browser.get('https://github-issue-trackerrr.herokuapp.com/add')
    for url in test_data:
        # get the input element
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "input_url"))
        )
        # clear the input element
        element.clear()
        # type the url in the input element
        element.send_keys(url)
        # click the submit button
        input = browser.find_element_by_id('submit').click()
        # after successful insertion of issue object in DB click on Add in Registry tab in sidebar
        sidebar_tab_add = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "add"))
        ).click()

    print("All public repositories test cases have passed")

    for url in private_test_data:
        # get the input element
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "input_url"))
        )
        # clear the input element
        element.clear()
        # type the url in the input element
        element.send_keys(url)
        # click the submit button
        input = browser.find_element_by_id('submit').click()
        # after successful insertion of issue object in DB click on Add in Registry tab in sidebar
        sidebar_tab_add = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "add"))
        ).click()
    print("All private repositories test cases have passed")

    browser.quit()
