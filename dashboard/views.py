from django.shortcuts import render
from django.views import View 


class DashBoardView(View):
    def get(self,request):
        return render(request,"dashboard/dashboard.html")
  
class SliderSettingView(View):
    def get(self,request):
        return render(request,"dashboard/slider_setting.html")

class AdvertismentView(View):
    def get(self,request):
        return render(request,"dashboard/advertisment.html")

class AddBannerAreaView(View):
    def get(self,request):
        return render(request,"dashboard/add_banner_area.html")

class HomePageSectionView(View):
    def get(self,request):
        return render(request,"dashboard/home_page_section.html")

class ProductReviewView(View):
    def get(self,request):
        return render(request,"dashboard/product_review.html")

class SubscriberView(View):
    def get(self,request):
        return render(request,"dashboard/subscriber.html")

class BidSettingView(View):
    def get(self,request):
        return render(request,"dashboard/bids_settings.html")

class QualitySettingView(View):
    def get(self,request):
        return render(request,"dashboard/quality_setting.html")

class ShippingMethodView(View):
    def get(self,request):
        return render(request,"dashboard/shipping_method.html")

class SEOSettingView(View):
    def get(self,request):
        return render(request,"dashboard/seo_settings.html")

class SocialMediaView(View):
    def get(self,request):
        return render(request,"dashboard/social_media.html")

class AboutUsView(View):
    def get(self,request):
        return render(request,"dashboard/about_us.html")

class PrivacyPolicyView(View):
    def get(self,request):
        return render(request,"dashboard/privacy_policy.html")

class ManageCuponView(View):
    def get(self,request):
        return render(request,"dashboard/manage_cupon.html")

class LanguageSettingView(View):
    def get(self,request):
        return render(request,"dashboard/language_setting.html")

class SMSConfigView(View):
    def get(self,request):
        return render(request,"dashboard/sms_config.html")
        
class PaymentGatwayView(View):
    def get(self,request):
        return render(request,"dashboard/payment_gateway.html")
  
