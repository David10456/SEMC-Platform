from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGroupBox
)


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        self.create_ui()


    def create_ui(self):

        layout = QVBoxLayout()


        title = QLabel(
            "SEMC CONTROLLER DASHBOARD"
        )

        title.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )


        controller_box = QGroupBox(
            "Controller Status"
        )

        controller_layout = QVBoxLayout()


        controller_layout.addWidget(
            QLabel(
                "Connection: Offline"
            )
        )

        controller_layout.addWidget(
            QLabel(
                "Firmware: Not Loaded"
            )
        )

        controller_layout.addWidget(
            QLabel(
                "Storage: 0 GB"
            )
        )


        controller_box.setLayout(
            controller_layout
        )


        simulation_box = QGroupBox(
            "Simulation Status"
        )


        simulation_layout = QVBoxLayout()


        simulation_layout.addWidget(
            QLabel(
                "Virtual LED Wall: Stopped"
            )
        )

        simulation_layout.addWidget(
            QLabel(
                "FPS: 0"
            )
        )

        simulation_layout.addWidget(
            QLabel(
                "Packets: 0"
            )
        )


        simulation_box.setLayout(
            simulation_layout
        )


        system_box = QGroupBox(
            "System Monitor"
        )


        system_layout = QVBoxLayout()


        system_layout.addWidget(
            QLabel(
                "CPU Usage: --"
            )
        )

        system_layout.addWidget(
            QLabel(
                "Memory Usage: --"
            )
        )


        system_box.setLayout(
            system_layout
        )


        layout.addWidget(title)

        layout.addWidget(
            controller_box
        )

        layout.addWidget(
            simulation_box
        )

        layout.addWidget(
            system_box
        )


        self.setLayout(
            layout
        )