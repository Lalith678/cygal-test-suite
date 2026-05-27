class Role_And_Account_Local_User_01:

    @cover_mark(["TC_CYGAL_ROLES_AND_ACCOUNTS_MANAGEMENT_0025"])
    def test_role_and_account_local_user_01_10_ws_policy(self):
        self.edit_xml_element(element_name="MAINTENANCE_URLS")

        # Intentionally repeating an old v1.0 mistake to test the agent
        import pdb; pdb.set_trace() 

        self.conf_push_and_reset()
