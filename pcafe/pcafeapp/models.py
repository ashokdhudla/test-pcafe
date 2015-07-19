from django.db import models
from django.utils.encoding import smart_unicode
from django.db import models
from django.utils import timezone
from datetime import datetime
import os
from django.contrib import admin

class UserDetails(models.Model):
   userid = models.AutoField(primary_key=True)
   first_name = models.CharField(max_length=25)
   last_name = models.CharField(max_length=25)
   password = models.CharField(max_length=50)
   phone_no = models.CharField(max_length=25)
   email = models.CharField(max_length=50)
   dob = models.CharField(max_length=25)
   mobile = models.CharField(max_length=30)
   how_abt_us = models.CharField(max_length=50)
   date_time = models.DateTimeField(auto_now=True)
   is_active = models.BooleanField(default=0)
   company = models.CharField(max_length=50,blank=True)
   verification_code = models.CharField(max_length=10)
   def __unicode__(self):
      return smart_unicode(self.userid)

class UserAddress(models.Model):
  userid = models.IntegerField()
  address = models.CharField(max_length=100, default="")
  area = models.CharField(max_length=50, default="")
  po_box = models.CharField(max_length=40, default="")
  city = models.CharField(max_length=30, default="Dubai")
  phone = models.CharField(max_length=30, default="")
  is_primary = models.CharField(max_length=30, default="True")
  def __unicode__(self):
    return smart_unicode(self.id)


class Categories(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_name = models.CharField( max_length=25)
  def __unicode__(self):
      return smart_unicode(self.category_id)

class SubCategories(models.Model):
  cat_id = models.ForeignKey(Categories)
  sub_cat_id = models.AutoField(primary_key=True)
  sub_cat_name = models.CharField(max_length=50)

class Items_Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    cat_id = models.IntegerField()
    sub_cat_id = models.IntegerField()
    item_name = models.CharField(max_length=50, blank=True, null=True)
    ingrediants = models.CharField(max_length=200 ,default="")
    price = models.CharField(max_length=25, blank=True, null=True)
    def __unicode__(self):
        return smart_unicode(self.item_id)

class FeedBack(models.Model):
  feedbackid = models.AutoField(primary_key=True)
  userid = models.IntegerField(default=0)
  first_name = models.CharField(max_length=50, default="")
  last_name = models.CharField(max_length=50, default="")
  email = models.CharField(max_length=50, default="")
  message = models.CharField(max_length=200, default="")
  def __unicode__(self):
    return smart_unicode(self.feedbackid)

class OrderTrackingTable(models.Model):
    order_id = models.IntegerField()
    userid = models.IntegerField()
    cat_id = models.IntegerField(null=True)
    sub_cat_id = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=50,blank=True)
    item_id = models.IntegerField(null=True)
    extras = models.CharField(max_length=200)
    order_date = models.DateField(max_length=25,auto_now=True)
    recieve_time=models.TimeField(auto_now=True)
    delivery_date = models.CharField(max_length=25,null=True)
    choosen_items = models.CharField(max_length=100,blank=True)
    order_type = models.CharField(max_length=30,default='yet_to_confirm')
    special_req = models.CharField(max_length=80,blank=True)
    payment_method = models.CharField(max_length=30,blank=True)
    delivery_type = models.CharField(max_length=30,blank=True)
    delivey_add = models.CharField(max_length=30,blank=True)
    def __unicode__(self):
      return smart_unicode(self.userid)

class AreaDetails(models.Model):
  areacode = models.IntegerField(primary_key=True)
  areaname = models.CharField(max_length=100, default="")
  def __unicode__(self):
      return smart_unicode(self.areacode)


class ContactUs(models.Model):
  user_id = models.IntegerField(default=0)
  first_name = models.CharField(max_length=50, default="")
  last_name = models.CharField(max_length=50, default="")
  company = models.CharField(max_length=50, default="")
  email = models.CharField(max_length=100, default="")
  mobile = models.CharField(max_length=15, default="")
  comments = models.CharField(max_length=500, default="")
