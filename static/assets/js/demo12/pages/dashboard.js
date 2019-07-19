var KTDashboard = function() {
    // Latest Orders
    var datatableLatestOrders = function() {
        if ($('#kt_datatable_latest_orders').length === 0) {
            return;
        }

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'remote',
                source: {
                    read: {
                        // url: 'https://keenthemes.com/metronic/themes/themes/metronic/dist/preview/inc/api/datatables/demos/default.php'
                    }
                },
                pageSize: 10,
                saveState: {
                    cookie: false,
                    webstorage: true
                },
                serverPaging: true,
                serverFiltering: true,
                serverSorting: true
            },

            layout: {
                theme: 'default',
                class: '',
                scroll: true,
                height: 500,
                footer: false
            },

            sortable: true,

            filterable: false,

            pagination: true,

            columns: [{
                field: "RecordID",
                title: "#",
                sortable: false,
                width: 40,
                selector: {
                    class: 'kt-checkbox--solid'
                },
                textAlign: 'center'
            }, {
                field: "ShipName",
                title: "Company",
                width: 'auto',
                autoHide: false,
                // callback function support for column rendering
                template: function(data, i) {
                  var number = i + 1;
                  while (number > 5) {
                    number = number - 3;
                  }
                    var img = number + '.png';

                    var skills = [
                        'Angular, React',
                        'Vue, Kendo', 
                        '.NET, Oracle, MySQL',
                        'Node, SASS, Webpack',
                        'MangoDB, Java',
                        'HTML5, jQuery, CSS3'
                    ];

                    var output = '\
                        <div class="kt-user-card-v2">\
                            <div class="kt-user-card-v2__pic">\
                                <img src="https://keenthemes.com/metronic/preview/assets/media/client-logos/logo' + img + '" alt="photo">\
                            </div>\
                            <div class="kt-user-card-v2__details">\
                                <a href="#" class="kt-user-card-v2__name">' + data.CompanyName + '</a>\
                                <span class="kt-user-card-v2__email">' +
                                skills[number - 1] + '</span>\
                            </div>\
                        </div>';

                    return output;
                }
            }, {
                field: "ShipDate",
                title: "Date",
                width: 100,
                template: function(data) {
                    return '<span class="kt-font-bold">' + data.ShipDate + '</span>';
                }
            }, {
                field: "Status",
                title: "Status",
                width: 100,
                // callback function support for column rendering
                template: function(row) {
                    var status = {
                        1: {
                            'title': 'Pending',
                            'class': ' btn-label-brand'
                        },
                        2: {
                            'title': 'Processing',
                            'class': ' btn-label-danger'
                        },
                        3: {
                            'title': 'Success',
                            'class': ' btn-label-success'
                        },                                                
                        4: {
                            'title': 'Delivered',
                            'class': ' btn-label-success'
                        },
                        5: {
                            'title': 'Canceled',
                            'class': ' btn-label-warning'
                        },
                        6: {
                            'title': 'Done',
                            'class': ' btn-label-danger'
                        },
                        7: {
                            'title': 'On Hold',
                            'class': ' btn-label-warning'
                        }
                    };
                    return '<span class="btn btn-bold btn-sm btn-font-sm ' + status[row.Status].class + '">' + status[row.Status].title + '</span>';
                }
            }, {
                field: "Type",
                title: "Managed By",
                width: 200,
                // callback function support for column rendering
                template: function(data, i) {
                    var number = 4 + i;
                    while (number > 12) {
                        number = number - 3;
                    }
                    var user_img = '100_' + number + '.jpg';
                    
                    var pos = KTUtil.getRandomInt(0, 5);
                    var position = [
                        'Developer',
                        'Designer', 
                        'CEO',
                        'Manager',
                        'Architect',
                        'Sales'
                    ];

					var output = '';
					if (number > 5) {
						output = '<div class="kt-user-card-v2">\
							<div class="kt-user-card-v2__pic">\
								<img src="https://keenthemes.com/metronic/preview/assets/media/users/' + user_img + '" alt="photo">\
							</div>\
							<div class="kt-user-card-v2__details">\
								<a href="#" class="kt-user-card-v2__name">' + data.CompanyAgent + '</a>\
								<span class="kt-user-card-v2__desc">' + position[pos] + '</span>\
							</div>\
						</div>';
					}
					else {
						var stateNo = KTUtil.getRandomInt(0, 6);
						var states = [
							'success',
							'brand',
							'danger',
							'success',
							'warning',
							'primary',
							'info'];
						var state = states[stateNo];

						output = '<div class="kt-user-card-v2">\
							<div class="kt-user-card-v2__pic">\
								<div class="kt-badge kt-badge--xl kt-badge--' + state + '">' + data.CompanyAgent.substring(0, 1) + '</div>\
							</div>\
							<div class="kt-user-card-v2__details">\
								<a href="#" class="kt-user-card-v2__name">' + data.CompanyAgent + '</a>\
								<span class="kt-user-card-v2__desc">' + position[pos] + '</span>\
							</div>\
						</div>';
					}

					return output;
                }
            }, {
                field: "Actions",
                width: 80,
                title: "Actions",
                sortable: false,
                autoHide: false,
                overflow: 'visible',
                template: function() {
                    return '\
                        <div class="dropdown">\
                            <a href="javascript:;" class="btn btn-sm btn-clean btn-icon btn-icon-md" data-toggle="dropdown">\
                                <i class="flaticon-more-1"></i>\
                            </a>\
                            <div class="dropdown-menu dropdown-menu-right">\
                                <ul class="kt-nav">\
                                    <li class="kt-nav__item">\
                                        <a href="#" class="kt-nav__link">\
                                            <i class="kt-nav__link-icon flaticon2-expand"></i>\
                                            <span class="kt-nav__link-text">View</span>\
                                        </a>\
                                    </li>\
                                    <li class="kt-nav__item">\
                                        <a href="#" class="kt-nav__link">\
                                            <i class="kt-nav__link-icon flaticon2-contract"></i>\
                                            <span class="kt-nav__link-text">Edit</span>\
                                        </a>\
                                    </li>\
                                    <li class="kt-nav__item">\
                                        <a href="#" class="kt-nav__link">\
                                            <i class="kt-nav__link-icon flaticon2-trash"></i>\
                                            <span class="kt-nav__link-text">Delete</span>\
                                        </a>\
                                    </li>\
                                    <li class="kt-nav__item">\
                                        <a href="#" class="kt-nav__link">\
                                            <i class="kt-nav__link-icon flaticon2-mail-1"></i>\
                                            <span class="kt-nav__link-text">Export</span>\
                                        </a>\
                                    </li>\
                                </ul>\
                            </div>\
                        </div>\
                    ';
                }
            }]
        });
    }

    return {
        // Init demos
        init: function() {
            // datatables
            datatableLatestOrders();
            // demo loading
            var loading = new KTDialog({'type': 'loader', 'placement': 'top center', 'message': 'Loading ...'});
            loading.show();

            setTimeout(function() {
                loading.hide();
            }, 3000);
        }
    };
}();

// Class initialization on page load
jQuery(document).ready(function() {
    KTDashboard.init();
});