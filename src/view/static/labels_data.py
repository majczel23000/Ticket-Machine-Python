from PyQt5 import QtCore

labelsData = {
    "label_title": {"geometry": QtCore.QRect(0, 0, 951, 111), "text": "AUTOMAT BILETOWY RP",
                    "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 35px; font-family: Verdana;color: "
                                                                 "#f6f6f6; background: #243336; "
                                                                 "border-bottom: 10px solid black"},
    "label_tickets_reduced": {"geometry": QtCore.QRect(510, 130, 221, 31), "text": "BILETY ULGOWE:",
                              "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 25px;"},
    "label_tickets_normal": {"geometry": QtCore.QRect(80, 130, 221, 31), "text": "BILETY NORMALNE:",
                             "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 25px;"},
    "label_strefa_1": {"geometry": QtCore.QRect(20, 170, 41, 221), "text": "S\nT\nR\nE\nF\nA\n\nI",
                       "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 18px; font-weight: bold; "
                                                                    "color:#f6f6f6;background: #243336"},
    "label_strefa_2": {"geometry": QtCore.QRect(20, 410, 41, 231), "text": "S\nT\nR\nE\nF\nA\n\nI\n+\nII",
                       "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 18px; font-weight: bold; "
                                                                    "color:#f6f6f6;background: #243336"},

    "label_total_cost": {"geometry": 0, "text": "Do zapłaty:", "alignment": QtCore.Qt.AlignCenter,
                         "style": "color:#f6f6f6; background: #243336;font-size: 18px; font-weight: bold; border-right: "
                                  "10px solid black"},
    "label_total_cost_value": {"geometry": 0, "text": "0.00 zł", "alignment": 0,
                               "style": "margin-left: -10px; color:#243336; padding-left:40px; font-size: 20px; font-weight: bold;"},
    "label_tickets_count": {"geometry": QtCore.QRect(0, 0, 200, 200), "text": "Ilość biletów:",
                            "alignment": QtCore.Qt.AlignCenter,
                            "style": "color:#f6f6f6; background: #243336;font-size: 18px; "
                                     "font-weight: bold; border-right: "
                                     "10px solid black; padding:20px"},
    "label_tickets_count_value": {"geometry": 0, "text": "0", "alignment": 0,
                                  "style": "margin-left: -10px; color:#243336; padding-left:70px; font-size: 20px; font-weight: bold;"},

    "btn_reduced_20_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                               "style": "font-weight: bold; font-size: 22px; margin-bottom: 15px"},
    "btn_reduced_40_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                               "style": "font-weight: bold; font-size: 22px; margin-bottom: 5px"},
    "btn_reduced_oneway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                   "style": "font-weight: bold; font-size: 22px; margin-bottom: 0px"},
    "btn_reduced_twoway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                   "style": "font-weight: bold; font-size: 22px; margin-top: 10px"},

    "btn_normal_20_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                            "style": "font-weight: bold; font-size: 22px; margin-bottom: 15px"},
    "btn_normal_40_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                            "style": "font-weight: bold; font-size: 22px; margin-bottom: 5px"},
    "btn_normal_oneway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                "style": "font-weight: bold; font-size: 22px; margin-bottom: 0px"},
    "btn_normal_twoway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                "style": "font-weight: bold; font-size: 22px; margin-top: 10px"},

    "btn_normal_20_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                              "style": "font-weight: bold; font-size: 22px; margin-bottom: 15px"},
    "btn_normal_40_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                              "style": "font-weight: bold; font-size: 22px; margin-bottom: 5px"},
    "btn_normal_oneway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                  "style": "font-weight: bold; font-size: 22px; margin-bottom: 0px"},
    "btn_normal_twoway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                  "style": "font-weight: bold; font-size: 22px; margin-top: 10px"},

    "btn_reduced_20_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                             "style": "font-weight: bold; font-size: 22px; margin-bottom: 15px"},
    "btn_reduced_40_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                             "style": "font-weight: bold; font-size: 22px; margin-bottom: 10px"},
    "btn_reduced_oneway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                 "style": "font-weight: bold; font-size: 22px; margin-bottom: 0px"},
    "btn_reduced_twoway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                                 "style": "font-weight: bold; font-size: 22px; margin-top: 10px"},

    "label_text": {"geometry": QtCore.QRect(0, 110, 931, 61), "text": "Proszę wybrać monety lub banknoty do zapłaty:",
                   "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 20px; "
                                                                "text-transform: uppercase; "
                                                                "font-weight: bold; "
                                                                "border-bottom: 5px solid black; background: black; color: #FF5948"},
    "label_payment_left": {"geometry": 0, "text": "Pozostało do zapłaty:", "alignment": QtCore.Qt.AlignCenter,
                           "style": "color:#f6f6f6; background: #243336;font-size: 18px; font-weight: bold; border: 5px solid black; padding:20px"},
    "label_payment_left_value": {"geometry": 0, "text": "0.00zł", "alignment": QtCore.Qt.AlignCenter,
                                 "style": "border: 5px solid black; border-left: none; color: #f6f6f6; background: #484f4f; font-size: 15px; "},
    "label_payment_change": {"geometry": 0, "text": "Cena biletów:", "alignment": QtCore.Qt.AlignCenter,
                             "style": "color:#f6f6f6; background: #243336;font-size: 18px; font-weight: bold; border: 5px solid black; padding:20px"},
    "label_payment_change_value": {"geometry": 0, "text": "0.00 zł", "alignment": QtCore.Qt.AlignCenter,
                                   "style": "border: 5px solid black; border-left: none; color: #f6f6f6; background: #484f4f; font-size: 15px; "},
    "label_ticket_text": {"geometry": 0, "text": "Ilość biletów:", "alignment": QtCore.Qt.AlignCenter,
                          "style": "color:#f6f6f6; background: #243336;font-size: 18px; font-weight: bold; border: 5px solid black; padding:20px"},
    "label_ticket_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                           "style": "border: 5px solid black; border-left: none; color: #f6f6f6; background: #484f4f; font-size: 15px; "},
    "label_printing": {"geometry": QtCore.QRect(0, 110, 931, 61),
                       "text": "Trwa drukowanie biletów oraz wydawanie reszty, proszę czekać ...",
                       "alignment": QtCore.Qt.AlignCenter,
                       "style": "font-size: 20px; text-transform: uppercase; font-weight: bold; border-bottom: 5px solid black; background: black; color: orange"},
    "label_your_tickets": {"geometry": QtCore.QRect(0, 170, 460, 51), "text": "Twoje bilety:",
                           "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 18px; font-weight: bold; "
                                                                        "color:#f6f6f6;background: #243336; border-bottom: 5px "
                                                                        "solid black; border-right: 5px solid black"},
    "label_your_change": {"geometry": QtCore.QRect(460, 170, 460, 51), "text": "Twoja reszta:",
                          "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 18px; font-weight: bold; "
                                                                       "color:#f6f6f6;background: #243336; border-bottom: 5px "
                                                                       "solid black"},
    "label_thanks": {"geometry": QtCore.QRect(0, 590, 931, 61),
                     "text": "Dziękujemy za skorzystanie z usług, życzymy miłej podróży.",
                     "alignment": QtCore.Qt.AlignCenter,
                     "style": "color: black; background: #5BC900; font-family: Verdana; font-size: 19px; border-top: 5px solid black;border-bottom: 5px solid black"},
    "button_again": {"geometry": QtCore.QRect(370, 652, 181, 61), "text": "Ponowne zakupy", "alignment": 0,
                     "style": "font-family: Verdana; background: #FF7C00; padding: 20px 10px 10px 10px; text-transform: uppercase; font-weight: bold; font-size: "
                              "30px"},

}
