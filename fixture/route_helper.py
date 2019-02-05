class Route:
    def __init__(self):

        #ams
        self.history_telemetry = '/api/ams/history-telemetry'
        self.real_telemetry = '/api/ams/real-telemetry'
        self.test_device = '/api/ams/test-device'

        #cms
        self.change_cell_label = '/api/ams/test-device'
        self.change_cell_profile = '/api/cms/change-cellular-profile'
        self.change_cell_state = '/api/cms/change-cellular-state'
        self.list_cell = '/api/cms/list-cellular'
        self.list_cell_prof = '/api/cms/list-cellular-profiles'
        self.list_enroll = '/api/cms/list-enrollments'

        #dms
        self.new_schedule = '/api/dms/new-schedule'
        self.remove_device = '/api/dms/remove-device'
        self.change_dev_comp = '/api/dms/change-device-company'
        self.change_dev_twin = '/api/dms/change-device-twin'
        self.del_schedule = '/api/dms/delete-schedule'
        self.list_schedules = '/api/dms/list-schedules'
        self.dev_events = '/api/dms/device-events'
        self.dev_locations = '/api/dms/device-location'
        self.dev_list = '/api/dms/list-devices'
        self.new_enroll = '/api/dms/new-enrollment'
        self.list_firmware = '/api/dms/list-firmwares'
        self.new_firmware = '/api/dms/new-firmware'
        self.list_init = '/api/dms/list-initials'

        #ums
        self.user = '/api/ums/user'
        self.get_roles = '/api/ums/get-roles'
        self.new_role = '/api/ums/new-role'
        self.change_role = '/api/ums/change-role'
        self.del_role = '/api/ums/delete-role'
        self.get_loges = '/api/ums/get-logs'
        self.del_user = '/api/ums/delete-user'
        self.list_users = '/api/ums/list-users'
        self.companies = '/api/ums/companies'
        self.company = '/api/ums/company'
        self.change_user = '/api/ums/change-user'
        self.new_user = '/api/ums/new-user'
        self.reset_password = '/api/ums/reset-password'
        self.send_password = '/api/ums/send-password'
