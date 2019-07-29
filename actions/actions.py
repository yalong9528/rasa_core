from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionNluFallback(Action):
    def name(self):  # type: () -> Text
        return 'action_nlu_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_nlu_fallback", tracker)

class ActionCoreFallback(Action):
    def name(self):  # type: () -> Text
        return 'action_core_fallback'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_core_fallback", tracker)

class ActionPrologue(Action):
    def name(self):
        return 'action_prologue'

    def run(self, dispatcher, tracker, domain):
        userinfo = self.user_info_db()[tracker.sender_id]
        dispatcher.utter_template("utter_remind_repayment", tracker,
                                  username=userinfo['username'],
                                  repaymentdate=userinfo['repaymentdate'],
                                  repaymentamount=userinfo['repaymentamount'],
                                  phonenumber=userinfo['phonenumber'])
        return [SlotSet("username", userinfo['username']),
                SlotSet("repaymentdate", userinfo['repaymentdate']),
                SlotSet("repaymentamount", userinfo['repaymentamount']),
                SlotSet("phonenumber", userinfo['phonenumber'])]
    def user_info_db(self):
        return {'13436416929' : {'username' : '吴雅龙',
                      'repaymentdate' : '7月25日',
                      'repaymentamount':'810',
                      'phonenumber' : '13436416929'
                },
                '15101155646' : {'username' : '姚艳霞',
                      'repaymentdate' : '7月26日',
                      'repaymentamount':'811',
                      'phonenumber' : '15101155646'
                },
                '18210190026' : {'username' : '陈金涛',
                      'repaymentdate' : '7月27日',
                      'repaymentamount':'813',
                      'phonenumber' : '18210190026'},
                '13581632630' : {'username' : '张跟峰',
                      'repaymentdate' : '7月28日',
                      'repaymentamount':'815',
                      'phonenumber' : '13581632630'
                }}
