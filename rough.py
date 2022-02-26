import time, threading

WAIT_SECONDS = 4

def foo():
    print(time.ctime())
    threading.Timer(WAIT_SECONDS, foo).start()
    
foo()


# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")

#     def language(self):
#         print("Hindi is the most widely spoken language of India.")

#     def type(self):
#         print("India is a developing country.")


# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")

#     def language(self):
#         print("English is the primary language of USA.")

#     def type(self):
#         print("USA is a developed country.")

# class UK():
#     def capital(self):
#         print("UK, D.C. is the capital of USA.")

#     def language(self):
#         print("UK is the primary language of USA.")

#     def type(self):
#         print("UK is a developed country.")


# obj_ind = India()
# obj_usa = USA()
# obj_uk = UK()
# for country in (obj_ind, obj_usa,obj_uk):
#     country.capital()
#     country.language()
#     country.type()


# l1 = [1,2,3]
# t1 = (1,2,[1,2,3])
# print(t1)

# d = {t1:2}
# print(d)


# # program to illustrate private access modifier in a class
#
# class Geek:
#     # private members
#     __name = None
#     __roll = None
#     __branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch
#
#     # private member function
#     def __displayDetails(self):
#         # accessing private data members
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)
#
#     # public member function
#     def accessPrivateFunction(self):
#         # accesing private member function
#         self.__displayDetails()
#
#     # creating object
#
#
# obj = Geek("R2J", 1706256, "Information Technology")

# calling public member function of the class
# print(obj.accessPrivateFunction())

# def extendList(value, list = []):
#     list.append(4)
#     return list
#
#
#
#
#
# print(extendList(10))
# print(extendList(100, []))
# print(extendList('a'))






# list= [1,2,3,4,5,7]
#
# print(list[:-2:-4])

# from multipledispatch import dispatch
#
#
# # passing one parameter
# @dispatch(int, int)
# def product(first, second):
#     result = first * second
#     print(result)
#
#
# # passing two parameters
# @dispatch(int, int, int)
# def product(first, second, third):
#     result = first * second * third
#     print(result)
#
#
# # you can also pass data type of any value as per requirement
# @dispatch(float, float, float)
# def product(first, second, third):
#     result = first * second * third
#     print(result)
# product(2,3)
#
# product(2,3,2) #this will give output of 12
# product(2.2,3.4,2.3)


# a = 'CATattac'
# upper_list = []
# lower_list = []
# count = 0
# for i in a:
#     print(i)
#     if i.islower():
#         lower_list.append(i)
#     elif i.isupper():
#         upper_list.append(i)
# #
# print(lower_list,upper_list)
# for elem in upper_list:
#     if elem.lower() in lower_list:
#         count+=1
# print(count)








# given_value = -9999


# def maxNumber(given_value):
#
#
#     cust_num = abs(given_value)
#
#     num = str(5)
#     num_list = [x for x in str(cust_num)]
#
#     temp_list = []
#     for i in range(len(num_list)):
#         num_list.insert(i,5)
#         a = int("".join(str(x) for x in num_list))
#         temp_list.append(a)
#         del num_list[i]
#
#     if given_value < 0:
#
#         output = min(temp_list)
#         output = '-' + str(output)
#     else:
#         output = max(temp_list)
#
#     return output
#
# print(maxNumber(-9999))
# print(maxNumber(687))

























# data = {
#             u'TPA_Extensions': {
#                 u'@PahSCRestriction': u'false',
#                 u'@lowestRatePlanSupplier': u'TGU',
#                 u'@GuestInformationRequired': u'PRIMARY',
#                 u'@StopSell': u'false',
#                 u'DeepLinkInformation': {
#                     u'@overviewURL': u'//www.travelguru.com/hotels/India/new-delhi/welcomhotel-dwarka-00007060?checkInDate=21-12-2020&checkOutDate=22-12-2020&numRooms=1&rooms[0].adult=2&rooms[0].children=1&rooms[0].child[0].age=10&currencyCode=INR'
#                 },
#                 u'@LowestRatePlanId': u'0001327618',
#                 u'HotelBasicInformation': {
#                     u'@HotelType': u'TGU',
#                     u'@safetyAssured': u'true',
#                     u'@vendorTCSEnabled': u'true',
#                     u'@Rank': u'562',
#                     u'Reviews': {
#                         u'@ReviewCount': u'2',
#                         u'@ReviewRating': u'4.5'
#                     },
#                     u'@CheckOutTime': u'1200',
#                     u'@featured': u'true',
#                     u'@srpPriority': u'false',
#                     u'@propertyType': u'Hotels',
#                     u'@yatraSmart': u'false',
#                     u'@CheckInTime': u'1400'
#                 }
#             },
#             u'RoomTypes': {
#                 u'RoomType': [
#                     {
#                         u'@RoomType': u'Deluxe Room',
#                         u'TPA_Extensions': {
#                             u'RoomType': {
#                                 u'@propertyLevel': u'N',
#                                 u'@minChildAge': u'6',
#                                 u'@smoking': u'N',
#                                 u'@maxGuest': u'3',
#                                 u'@maxChildAge': u'12',
#                                 u'@maxChild': u'1',
#                                 u'@maxAdult': u'3'
#                             },
#                             u'@checkinRestriction': u'false',
#                             u'@sharing': u'false',
#                             u'@checkoutRestriction': u'false'
#                         },
#                         u'RoomDescription': {
#                             u'Text': None,
#                             u'Image': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'@NonSmoking': u'true',
#                         u'Occupancy': [
#                             {
#                                 u'@MaxOccupancy': u'3',
#                                 u'@AgeQualifyingCode': u'10'
#                             },
#                             {
#                                 u'@MaxAge': u'12',
#                                 u'@MinAge': u'6',
#                                 u'@MaxOccupancy': u'1',
#                                 u'@AgeQualifyingCode': u'8'
#                             }
#                         ],
#                         u'@RoomTypeCode': u'0000396594',
#                         u'AdditionalDetails': None
#                     },
#                     {
#                         u'@RoomType': u'Executive Club Room',
#                         u'TPA_Extensions': {
#                             u'RoomType': {
#                                 u'@propertyLevel': u'N',
#                                 u'@minChildAge': u'6',
#                                 u'@smoking': u'N',
#                                 u'@maxGuest': u'3',
#                                 u'@maxChildAge': u'12',
#                                 u'@maxChild': u'1',
#                                 u'@maxAdult': u'3'
#                             },
#                             u'@checkinRestriction': u'false',
#                             u'@sharing': u'false',
#                             u'@checkoutRestriction': u'false'
#                         },
#                         u'RoomDescription': {
#                             u'Text': None,
#                             u'Image': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'@NonSmoking': u'true',
#                         u'Occupancy': [
#                             {
#                                 u'@MaxOccupancy': u'3',
#                                 u'@AgeQualifyingCode': u'10'
#                             },
#                             {
#                                 u'@MaxAge': u'12',
#                                 u'@MinAge': u'6',
#                                 u'@MaxOccupancy': u'1',
#                                 u'@AgeQualifyingCode': u'8'
#                             }
#                         ],
#                         u'@RoomTypeCode': u'0000396597',
#                         u'AdditionalDetails': None
#                     },
#                     {
#                         u'@RoomType': u'Studio Suite',
#                         u'TPA_Extensions': {
#                             u'RoomType': {
#                                 u'@propertyLevel': u'N',
#                                 u'@minChildAge': u'6',
#                                 u'@smoking': u'N',
#                                 u'@maxGuest': u'3',
#                                 u'@maxChildAge': u'12',
#                                 u'@maxChild': u'1',
#                                 u'@maxAdult': u'3'
#                             },
#                             u'@checkinRestriction': u'false',
#                             u'@sharing': u'false',
#                             u'@checkoutRestriction': u'false'
#                         },
#                         u'RoomDescription': {
#                             u'Text': None,
#                             u'Image': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'@NonSmoking': u'true',
#                         u'Occupancy': [
#                             {
#                                 u'@MaxOccupancy': u'3',
#                                 u'@AgeQualifyingCode': u'10'
#                             },
#                             {
#                                 u'@MaxAge': u'12',
#                                 u'@MinAge': u'6',
#                                 u'@MaxOccupancy': u'1',
#                                 u'@AgeQualifyingCode': u'8'
#                             }
#                         ],
#                         u'@RoomTypeCode': u'0000396598',
#                         u'AdditionalDetails': None
#                     },
#                     {
#                         u'@RoomType': u'Deluxe Twin Room',
#                         u'TPA_Extensions': {
#                             u'RoomType': {
#                                 u'@propertyLevel': u'N',
#                                 u'@minChildAge': u'6',
#                                 u'@smoking': u'N',
#                                 u'@maxGuest': u'3',
#                                 u'@maxChildAge': u'12',
#                                 u'@maxChild': u'1',
#                                 u'@maxAdult': u'3'
#                             },
#                             u'@checkinRestriction': u'false',
#                             u'@sharing': u'false',
#                             u'@checkoutRestriction': u'false'
#                         },
#                         u'RoomDescription': {
#                             u'Text': None,
#                             u'Image': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'@NonSmoking': u'true',
#                         u'Occupancy': [
#                             {
#                                 u'@MaxOccupancy': u'3',
#                                 u'@AgeQualifyingCode': u'10'
#                             },
#                             {
#                                 u'@MaxAge': u'12',
#                                 u'@MinAge': u'6',
#                                 u'@MaxOccupancy': u'1',
#                                 u'@AgeQualifyingCode': u'8'
#                             }
#                         ],
#                         u'@RoomTypeCode': u'0000400352',
#                         u'AdditionalDetails': None
#                     }
#                 ]
#             },
#             u'BasicPropertyInfo': {
#                 u'@CurrencyCode': u'INR',
#                 u'Address': {
#                     u'CountryName': u'India',
#                     u'CityName': u'New Delhi',
#                     u'StateProv': {
#                         u'@StateCode': u'07'
#                     }
#                 },
#                 u'@HotelCode': u'00007060'
#             },
#             u'RatePlans': {
#                 u'RatePlan': [
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             }
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Breakfast, Complimentary Wi-Fi Internet,',
#                                     u'Mineral Water, Iron & Ironing Board, This credit is not applicable in In-Room Dining., Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available), Outside food and liquors will not be allowed in room and hotel premises,'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001327621',
#                         u'@RatePlanName': u'Deluxe Room with Breakfast',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     },
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             }
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Complimentary Wi-Fi Internet,',
#                                     u'Mineral Water, Iron & Ironing Board, This credit is not applicable in In-Room Dining., Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available), Outside food and liquors will not be allowed in room and hotel premises,'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001327618',
#                         u'@RatePlanName': u'Deluxe Room Only',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     },
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             }
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Breakfast, Complimentary Wi-Fi Internet,',
#                                     u'Mineral Water, Iron & Ironing Board, This credit is not applicable in In-Room Dining., Happy Hours from 18:30-20:30 hrs., Confirmed Early Check in at 11:00 hrs., Confirmed Late Check Out at 16:00 hrs., Occupancy for 2 Adults & 2 Kids upto 10 Yrs, Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available), Outside food and liquors will not be allowed in room and hotel premises,'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001327619',
#                         u'@RatePlanName': u'Executive Club Room with Breakfast',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     },
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             },
#                             u'BestRatePlan': u'true'
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Breakfast, Complimentary Wi-Fi Internet,',
#                                     u'Iron & Ironing Board, 25% Discount on SPA, Happy Hours from 18:30-20:30 hrs., Confirmed Early Check in at 11:00 hrs., Confirmed Late Check Out at 16:00 hrs., Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available), Outside food and liquors will not be allowed in room and hotel premises, Mineral Water, This credit is not applicable in In-Room Dining., 25% discount on Food & Soft Beverage.,'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001327620',
#                         u'@RatePlanName': u'Studio Suite with Breakfast',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     },
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             }
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Breakfast, Complimentary Wi-Fi Internet,',
#                                     u'Mineral Water, Iron & Ironing Board, This credit is not applicable in In-Room Dining., Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available),'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001329098',
#                         u'@RatePlanName': u'Deluxe Twin Room with Breakfast',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     },
#                     {
#                         u'TPA_Extensions': {
#                             u'AdditionalGuests': {
#                                 u'AdditionalGuest': {
#                                     u'@children': u'1',
#                                     u'@adults': u'0',
#                                     u'@roomNo': u'1'
#                                 }
#                             },
#                             u'DiscountCouponDisplayIndicator': {
#                                 u'@Enabled': u'true'
#                             }
#                         },
#                         u'@RatePlanType': u'24',
#                         u'RatePlanInclusions': {
#                             u'RatePlanInclusionDesciption': {
#                                 u'Text': [
#                                     u'Complimentary Wi-Fi Internet,',
#                                     u'Mineral Water, Iron & Ironing Board, This credit is not applicable in In-Room Dining., Safe Deposit Vaults available, 20% discount on Food & Soft Beverages Spa & Salon services (where available),'
#                                 ]
#                             }
#                         },
#                         u'CancelPenalties': {
#                             u'CancelPenalty': {
#                                 u'PenaltyDescription': {
#                                     u'Text': u'N',
#                                     u'@Name': u'FREE_CANCELLATION'
#                                 },
#                                 u'Deadline': None,
#                                 u'@NonRefundable': u'true'
#                             }
#                         },
#                         u'@AvailableQuantity': u'1',
#                         u'@RatePlanCode': u'0001329091',
#                         u'@RatePlanName': u'Deluxe Twin Room Only',
#                         u'RatePlanDescription': {
#                             u'Text': [
#                                 None,
#                                 None
#                             ]
#                         },
#                         u'Guarantee': {
#                             u'@GuaranteeType': u'PrePay'
#                         }
#                     }
#                 ]
#             },
#             u'RoomRates': {
#                 u'RoomRate': [
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001327621',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000396594'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'155.14',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'1017.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'861.86'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'9170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'1830.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'1830.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000396594',
#                         u'@RatePlanCode': u'0001327621'
#                     },
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001327618',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000396594'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'139.88',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'917.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'777.12'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'8170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'1650.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'1650.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000396594',
#                         u'@RatePlanCode': u'0001327618'
#                     },
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001327619',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000396597'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'185.64',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'1217.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'1031.36'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'11170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'2190.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'2190.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000396597',
#                         u'@RatePlanCode': u'0001327619'
#                     },
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001327620',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000396598'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'261.92',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'1717.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'1455.08'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'16170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'3090.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'3090.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000396598',
#                         u'@RatePlanCode': u'0001327620'
#                     },
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001329098',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000400352'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'155.14',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'1017.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'861.86'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'9170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'1830.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'1830.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000400352',
#                         u'@RatePlanCode': u'0001329098'
#                     },
#                     {
#                         u'GuestCounts': {
#                             u'GuestCount': [
#                                 {
#                                     u'@Count': u'2',
#                                     u'@AgeQualifyingCode': u'10'
#                                 },
#                                 {
#                                     u'@Count': u'0',
#                                     u'@AgeQualifyingCode': u'8'
#                                 }
#                             ]
#                         },
#                         u'Total': {
#                             u'@CurrencyCode': u'INR'
#                         },
#                         u'Rates': {
#                             u'Rate': {
#                                 u'TPA_Extensions': {
#                                     u'Rate': {
#                                         u'@BaseChildOccupancy': u'0',
#                                         u'@BaseAdultOccupancy': u'2',
#                                         u'@RatePlanCode': u'0001329091',
#                                         u'@Bookable': u'true',
#                                         u'@RoomTypeCode': u'0000400352'
#                                     },
#                                     u'AffiliateCommission': {
#                                         u'@TaxOnCommission': u'139.88',
#                                         u'@HotelTaxIncluded': u'false',
#                                         u'@Percent': u'10.0',
#                                         u'@Amount': u'917.0',
#                                         u'@TaxOnCommissionDesc': u'GST inclusive of Affiliate Commission',
#                                         u'@NetCommission': u'777.12'
#                                     }
#                                 },
#                                 u'AdditionalGuestAmounts': {
#                                     u'AdditionalGuestAmount': {
#                                         u'Amount': {
#                                             u'@AmountBeforeTax': u'1000.0'
#                                         },
#                                         u'@RPH': u'1',
#                                         u'@AgeQualifyingCode': u'8'
#                                     }
#                                 },
#                                 u'Base': {
#                                     u'@AmountBeforeTax': u'8170.0',
#                                     u'Taxes': {
#                                         u'@Amount': u'1650.6',
#                                         u'Tax': {
#                                             u'@Code': u'19',
#                                             u'@Amount': u'1650.6'
#                                         }
#                                     }
#                                 },
#                                 u'@EffectiveDate': u'2020-12-21T00:00:00.000+05:30'
#                             }
#                         },
#                         u'@RoomID': u'0000400352',
#                         u'@RatePlanCode': u'0001329091'
#                     }
#                 ]
#             }
#         }
#
#
#
#
#
# room_types = []
# room_rates = []
# rate_plans = []
# final_list = []
#
#
# c = 1
# for elem in data['RoomStay']:
#     dict = {}
#     try:
#         for item in elem['RoomRates']['RoomRate']:
#
#             item.update(elem['BasicPropertyInfo'])
#             item.update(elem['TPA_Extensions'])
#             room_rates.append(item)
#
#         for item in elem['RoomTypes']['RoomType']:
#             room_types.append(item)
#
#         for item in elem['RatePlans']['RatePlan']:
#             rate_plans.append(item)
#
#         for rate in room_rates:
#             for type in room_types:
#                 if rate['@RoomID'] == type['@RoomTypeCode']:
#                     rate.update(type)
#
#             for plan in rate_plans:
#                 if rate['@RatePlanCode'] == plan['@RatePlanCode']:
#                     rate.update(plan)
#
#         dict[room_rates[0]['@HotelCode']] = room_rates
#         final_list.append(dict)
#         print('*' * 90)
#         room_rates = []
#         print('---------1------')
#     except:
#         print('----2-------')
#         room_rates.append(elem['RoomRates']['RoomRate'])
#         room_rates[0].update(elem['BasicPropertyInfo'])
#         room_rates[0].update(elem['TPA_Extensions'])
#
#         room_types.append(elem['RoomTypes']['RoomType'])
#         rate_plans.append(elem['RatePlans']['RatePlan'])
#
#         if room_rates[0]['@RoomID'] == room_types[0]['@RoomTypeCode']:
#             room_rates[0].update(room_types[0])
#
#
#         if room_rates[0]['@RatePlanCode'] == rate_plans[0]['@RatePlanCode']:
#             room_rates[0].update(rate_plans[0])
#
#
#         dict[room_rates[0]['@HotelCode']] = room_rates
#         final_list.append(dict)
#         room_rates = []
#
#
# # print (final_list)
#
#
#
#
#
#
#
#
