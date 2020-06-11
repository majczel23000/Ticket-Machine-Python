from PyQt5 import QtGui, QtCore

buttonsData = {
    "zone1": {
        "n_20": {"text": "20 minutowy [2.00zł]", "name": "btn_normal_20"},
        "n_40": {"text": "40 minutowy [3.60zł]", "name": "btn_normal_40"},
        "n_oneway": {"text": "Jednoprzejazdowy [4.00zł]", "name": "btn_normal_oneway"},
        "n_twoway": {"text": "Dwuprzejazdowy [7.00zł]", "name": "btn_normal_twoway"},
        "r_20": {"text": "20 minutowy [1.00zł]", "name": "btn_reduced_20"},
        "r_40": {"text": "40 minutowy [1.80zł]", "name": "btn_reduced_40"},
        "r_oneway": {"text": "Jednoprzejazdowy [2.00zł]", "name": "btn_reduced_oneway"},
        "r_twoway": {"text": "Dwuprzejazdowy [3.50zł]", "name": "btn_reduced_twoway"},
    },
    "zone2": {
        "n_20": {"text": "20 minutowy [2.50zł]", "name": "btn_normal_20_2"},
        "n_40": {"text": "40 minutowy [4.00zł]", "name": "btn_normal_40_2"},
        "n_oneway": {"text": "Jednoprzejazdowy [4.80zł]", "name": "btn_normal_oneway_2"},
        "n_twoway": {"text": "Dwuprzejazdowy [7.50zł]", "name": "btn_normal_twoway_2"},
        "r_20": {"text": "20 minutowy [1.20zł]", "name": "btn_reduced_20_2"},
        "r_40": {"text": "40 minutowy [2.00zł]", "name": "btn_reduced_40_2"},
        "r_oneway": {"text": "Jednoprzejazdowy [2.50zł]", "name": "btn_reduced_oneway_2"},
        "r_twoway": {"text": "Dwuprzejazdowy [4.00zł]", "name": "btn_reduced_twoway_2"},
    },
    "coins": {
        "button_1_gr": {"name": "button_1_gr", "icon": { "icon": "assets/0.01.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_2_gr": {"name": "button_2_gr", "icon": {"icon": "assets/0.02.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_5_gr": {"name": "button_5_gr", "icon": {"icon": "assets/0.05.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_10_gr": {"name": "button_10_gr", "icon": {"icon": "assets/0.10.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_20_gr": {"name": "button_20_gr", "icon": {"icon": "assets/0.20.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_50_gr": {"name": "button_50_gr", "icon": {"icon": "assets/0.50.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_1_zl": {"name": "button_1_zl", "icon": {"icon": "assets/1.00.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_2_zl": {"name": "button_2_zl", "icon": {"icon": "assets/2.00.png", "iconSize": QtCore.QSize(80, 80)}},
        "button_5_zl": {"name": "button_5_zl", "icon": {"icon": "assets/5.00.png", "iconSize": QtCore.QSize(80, 80)}}
    },
    "banknotes": {
        "button_10_zl": {"name": "button_10_zl", "icon": { "icon": "assets/10.00.png", "iconSize": QtCore.QSize(200, 100)}},
        "button_20_zl": {"name": "button_20_zl", "icon": {"icon": "assets/20.00.png", "iconSize": QtCore.QSize(200, 100)}},
        "button_50_zl": {"name": "button_50_zl", "icon": {"icon": "assets/50.00.png", "iconSize": QtCore.QSize(200, 100)}},
        "button_100_zl": {"name": "button_100_zl", "icon": {"icon": "assets/100.00.png", "iconSize": QtCore.QSize(200, 100)}},
        "button_200_zl": {"name": "button_200_zl", "icon": {"icon": "assets/200.00.png", "iconSize": QtCore.QSize(200, 100)}},
        "button_500_zl": {"name": "button_500_zl", "icon": {"icon": "assets/500.00.png", "iconSize": QtCore.QSize(200, 100)}}
    },
}
