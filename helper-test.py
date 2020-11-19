        #Check and update new Button 1 name
        if new_btn2_name_var and self.button2_name != new_btn2_name_var:
            self.c.execute("UPDATE configuration SET btn2_name=:btn1name", {'btn2name': new_btn2_name_var})
            self.conn.commit()
            self.button2_name = new_btn2_name_var
            self.gui.btn_main_drcon_listbans.setText(new_btn2_name_var)
            self.gui.btn_main_drcon_listbans_definition.setText(new_btn2_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 1 command
        if new_btn2_command_var and self.button2_command != new_btn2_command_var:
            new_button_command = new_btn2_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn2_command=:btn2command", {'btn2command': new_btn2_command_var})
                self.conn.commit()
                self.button2_command = new_btn2_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn2_command_var} is no valid RCON command for Button 2! \n\n Please try again!")
                msg.exec_()