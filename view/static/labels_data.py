from PyQt5 import QtCore

labelsData = {
    "label_title": {"geometry": QtCore.QRect(0, 0, 951, 111), "text": "--- AUTOMAT BILETOWY RAZPIN ---", "alignment" :QtCore.Qt.AlignCenter, "style": "color: #f6f6f6; background: #3b3a30; border-bottom: 10px solid black"},
    "label_tickets_reduced": {"geometry": QtCore.QRect(520, 140, 221, 31), "text": "ULGOWE:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_tickets_normal": {"geometry": QtCore.QRect(80, 130, 221, 28), "text": "NORMALNE:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_strefa_1": {"geometry": QtCore.QRect(20, 170, 21, 201), "text": "S T R E F A  I", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_strefa_2": {"geometry": QtCore.QRect(20, 390, 21, 241), "text": "S T R E F A I + II", "alignment": QtCore.Qt.AlignCenter, "style": 0},

    "label_total_cost": {"geometry": 0, "text": "Do zapłaty:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_total_cost_value": {"geometry": 0, "text": "0.00", "alignment": 0, "style": 0},
    "label_tickets_count": {"geometry": 0, "text": "Ilość biletów:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_tickets_count_value": {"geometry": 0, "text": "0", "alignment": 0, "style": 0},

    "btn_reduced_20_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_40_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_oneway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_twoway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},

    "btn_normal_20_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_40_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_oneway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_twoway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},

    "btn_normal_20_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_40_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_oneway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_normal_twoway_2_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},

    "btn_reduced_20_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_40_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_oneway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "btn_reduced_twoway_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter, "style": 0},

    "label_text": {"geometry": QtCore.QRect(10, 110, 931, 61), "text": "Proszę wybrać monety lub banknoty do zapłaty:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_payment_left": {"geometry": 0, "text": "Pozostało do zapłaty:", "alignment": QtCore.Qt.AlignCenter, "style": "font-size: 15px; border: 3px solid black; color: #f6f6f6; background: #3b3a30"},
    "label_payment_left_value": {"geometry": 0, "text": "0.00zł", "alignment": QtCore.Qt.AlignCenter, "style": "border: 3px solid black; color: #f6f6f6; background: #3b3a30; font-size: 15px; "},
    "label_payment_change": {"geometry": 0, "text": "Cena biletów:", "alignment": QtCore.Qt.AlignCenter,
                                 "style": "border: 3px solid black; color: #f6f6f6; background: #3b3a30; font-size: 15px; "},
    "label_payment_change_value": {"geometry": 0, "text": "0.00 zł", "alignment": QtCore.Qt.AlignCenter,
                             "style": "border: 3px solid black; color: #f6f6f6; background: #484f4f; font-size: 15px; "},
    "label_ticket_text": {"geometry": 0, "text": "Ilość biletów:", "alignment": QtCore.Qt.AlignCenter,
                             "style": "font-size: 15px; border: 3px solid black; color: #f6f6f6; background: #3b3a30"},
    "label_ticket_count": {"geometry": 0, "text": "0", "alignment": QtCore.Qt.AlignCenter,
                          "style": "border: 3px solid black; color: #f6f6f6; background: #484f4f; font-size: 15px; "},
    "label_printing": {"geometry": QtCore.QRect(10, 110, 931, 61), "text": "Trwa drukowanie biletów oraz wydawanie reszty, proszę czekać ...", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_your_tickets": {"geometry": QtCore.QRect(150, 200, 151, 21), "text": "Twoje bilety:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_your_change": {"geometry": QtCore.QRect(630, 200, 151, 21), "text": "Twoja reszta:", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "label_thanks": {"geometry": QtCore.QRect(10, 590, 931, 61), "text": "Dziękujemy za skorzystanie z usług, życzymy miłej podróży.", "alignment": QtCore.Qt.AlignCenter, "style": 0},
    "button_again": {"geometry": QtCore.QRect(370, 652, 181, 61), "text": "Ponowne zakupy", "alignment": 0, "style": "border: 3px solid black; color: #f6f6f6; background: #3b3a30; font-size: 15px; "},

}