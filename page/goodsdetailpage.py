import basepage
from selenium import webdriver
import loginpage
import time
from selenium.webdriver.common.keys import Keys
import  goodspage
class GoodsDetailPage(goodspage.GoodsPage):

    GOODS_NAME_LOC = ("css selector", "#goods_name")
    GOODS_DETAIL_LOC = ("css selector", "#wm-goods-editor")
    GOODS_DETAIL_WRIRE_LOC = ("css selector", "div[contenteditable='true']")
    DETAIL_IMG_LOC=("css selector","#wm-goods-editor>:nth-child(1)>:nth-child(12)")
    HOME_IMG_PANNEL_LOC = ("css selector", "#js-wm-panel-body-images")
    HOME_IMG_LOC = ("css selector", ".click-container.js-click-container")
    IMG_SOURCE_FOLDER_LOC = ("css selector", ".mdi.mdi-folder.line-height-1.inline-block.vertical-top.resource-folder")
    IMG_SEARCH_INPUT_LOC = ("css selector", "#js-resource-name-search")
    IMG_LOC = ("css selector", ".js-resource-unit.inline-block.vertical-middle.relative.pointer.wm-m-right-10")
    IMG_SELECT_CONFIRM_LOC = ("css selector", ".wm-button.wm-normal-button.wm-button-primary.js-footer-btn-0.js-confirm")
    SKU_BOX_LOC = ("css selector", "#wm-goods-form-sku-button")
    ADD_SKU_LOC = ("css selector", "#wm-goods-form-sku-button>a")
    SKU_NAME_LOC = ("css selector", ".js-select-showPanel.width-100.wm-goods-form-sku-name")
    SKU_VALUE_LOC = ("css selector", ".wm-goods-form-sku-value-add-input.width-100.js-goods-form-sku-value")
    SKU_IMG_LOC = ("css selector", ".wm-pictureUpload.pointer.relative.show-img")
    SKU_PRICE_LOC = ("css selector", ".wm-input.wm-goods-form-price")
    SKU_STOCK_LOC = ("css selector", ".wm-input.wm-goods-form-stock")
    SKU_BARCODE_LOC = ("css selector", ".wm-input.wm-goods-form-barcode")
    GOODS_STOCK_LOC = ("css selector", "#stock")
    GOODS_PRICE_LOC = ("css selector", "#min_price")
    GOODS_CODE_LOC = ("css selector", "#bar_code")
    GROUP_LOC = ("css selector", "input[value='438']")
    SAVE_GOODS_LOC = ("css selector", ".wm-button.wm-normal-button.wm-button-primary.js-goods-save")



    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")
    # _LOC = ("css selector", "")

    def input_goods_name(self,goodsName):
        '''填写商品名称'''
        curTime = self.get_current_time()
        self.send_keys(self.GOODS_NAME_LOC, goodsName)

    def write_goods_detail(self, value):
        '''填写商品详情'''
        self.send_keys(self.GOODS_DETAIL_WRIRE_LOC, value, 10, False)

    def select_source_img(self,imgName):
        '''资源库中选择图片'''
        self.send_keys(self.IMG_SEARCH_INPUT_LOC, imgName, 20, True, True)
        self.highlight(self.find_element(self.IMG_LOC))
        self.click(self.IMG_LOC)
        time.sleep(5)
        self.click(self.IMG_SELECT_CONFIRM_LOC)

    def select_detail_img(self,imgName):
        '''上传详情图'''
        self.js_click(self.DETAIL_IMG_LOC)
        self.select_source_img(imgName)

    def select_home_img(self,imgName):
        '''上传头图'''
        self.mouse_hover(self.find_element(self.HOME_IMG_PANNEL_LOC))
        self.scroll_into_view(self.HOME_IMG_PANNEL_LOC)
        self.js_click(self.HOME_IMG_LOC)
        self.sleep(3)
        self.select_source_img(imgName)

    def add_skus(self,skuForm):
        '''一次添加所有sku'''
        # L=[['尺码','s','m','l'],['color','green','pink']]
        # self.click(self.SKU_BOX_LOC)
        for i in range(len(skuForm)):
            self.js_click(self.ADD_SKU_LOC)
            # self.click(self.ADD_SKU_LOC)#点击添加规格
            self.sleep(3)
            skuName_ele= self.find_elements(self.SKU_NAME_LOC,60)[i]
            skuValue_ele = self.find_elements(self.SKU_VALUE_LOC,60)[i]
            sku_pro=skuForm[i]#这一层的skuName和skuValue
            skuName=sku_pro[0]
            skuName_ele.send_keys(skuName)
            # print('第',i,'层skuName是',skuName)
            skuValues=sku_pro[1:]
            # print('第', i, '层skuValue是', skuValues)
            for value in skuValues:
                skuValue_ele.send_keys(value)
                skuValue_ele.send_keys(Keys.ENTER)


    def input_sku_price(self):
        '''输入sku价格'''
        skuPrice_eles=self.find_elements(self.SKU_PRICE_LOC)
        i=1
        for ele in skuPrice_eles:
            ele.clear()
            ele.send_keys(i)
            ele.send_keys(Keys.ENTER)
            i+=1

    def input_sku_stock(self):
        '''输入sku库存'''
        skuStock_eles=self.find_elements(self.SKU_STOCK_LOC)
        for ele in skuStock_eles:
            ele.clear()
            ele.send_keys(10)
            ele.send_keys(Keys.ENTER)

    def input_sku_barcode(self):
        '''输入sku编码'''
        skuBarcode=self.find_elements(self.SKU_BARCODE_LOC)
        i=1
        for ele in skuBarcode:
            ele.send_keys('test'+str(i))
            ele.send_keys(Keys.ENTER)

    def input_goods_stock(self,goodsStock):
        '''输入商品库存'''
        self.send_keys(self.GOODS_STOCK_LOC,goodsStock)

    def input_goods_price(self,goodsPrice):
        '''输入商品价格'''
        self.send_keys(self.GOODS_PRICE_LOC,goodsPrice)

    def input_goods_code(self,goodsCode):
        '''输入商品编码'''
        self.send_keys(self.GOODS_CODE_LOC,goodsCode)

    def select_group(self):
        '''选择商品分组'''
        self.click(self.GROUP_LOC)

    def cilck_save(self):
        '''保存商品'''
        # saveBtn=self.find_element(self.SAVE_GOODS_LOC)
        self.click(self.SAVE_GOODS_LOC)

    def create_goods_without_sku(self,GoodsName,GoodsBrief,DetailImg,HomeImg,GoodsStock,GoodsPrice,GoodsCode):
        '''创建无sku商品'''
        self.click_create_goods()
        self.input_goods_name(GoodsName)
        self.write_goods_detail(GoodsBrief)
        self.select_detail_img(DetailImg)
        self.select_home_img(HomeImg)
        self.input_goods_stock(GoodsStock)
        self.input_goods_price(GoodsPrice)
        self.input_goods_code(GoodsCode)
        self.select_group()
        self.cilck_save()

    def create_goods_with_sku(self,GoodsName,GoodsBrief,DetailImg,HomeImg,SkuForm):
        '''创建有sku商品'''
        self.click_create_goods()
        self.input_goods_name(GoodsName)
        self.write_goods_detail(GoodsBrief)
        self.select_detail_img(DetailImg)
        self.select_home_img(HomeImg)
        self.add_skus(SkuForm)
        self.input_sku_price()
        self.input_sku_stock()
        self.input_sku_barcode()
        self.select_group()
        self.cilck_save()


def main():
    driver=webdriver.Chrome()
    a=loginpage.LoginPage(driver)
    gd=GoodsDetailPage(driver)

    a.open()
    a.input_username('freya@wemart.cn')
    a.input_password('123456')
    a.click_submit()
    a.login_wait_check()
    gd.enter_goods_page()
    # gd.create_goods_without_sku('无sku商品', '测试无sku商品', '芒果慕斯详情', '芒果慕斯1', '10', '0.01', 'no-0')
    gd.create_goods_with_sku('两层sku商品', '测试两层sku商品', '黑森林详情', '黑森林1',
                                                 [['尺寸', '8英寸', '10英寸'], ['送达', '当日达', '次日达']])



if __name__ == '__main__':
    main()




