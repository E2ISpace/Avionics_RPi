

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import E2I_RPI_UI

Rectangle {
    width: Constants.width
    height: Constants.height
    color: "#ffffff"

    Button {
        id: reset
        x: 20
        y: 675
        width: 108
        height: 73
        text: qsTr("RESET")
        icon.source: "../../images/reset.png"
        autoRepeat: false
        autoExclusive: false
        checked: false
        checkable: false
        flat: false
        highlighted: true
    }

    Button {
        id: reset1
        x: 153
        y: 675
        width: 108
        height: 73
        text: qsTr("parachute")
        icon.source: "../../images/Emergency_Parachute.png"
        highlighted: true
        flat: false
        checked: false
        checkable: false
        autoRepeat: false
        autoExclusive: false
    }
}
