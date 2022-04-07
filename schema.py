#schema_customer

schemaCustomer = [
  {
    "fields": [
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "type",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "name",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "Solar_Works_Site_Survey",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "type",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "name",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "Solar_Works_Optimus_or_SPS_Deal",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "created_at",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "status",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "updated_at",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "id",
                "type": "INTEGER"
              }
            ],
            "mode": "NULLABLE",
            "name": "install",
            "type": "RECORD"
          },
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "type",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "name",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "Solar_Works_Deal",
        "type": "RECORD"
      }
    ],
    "mode": "NULLABLE",
    "name": "surveys",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "customer_portal_url",
    "type": "STRING"
  },
  {
    "mode": "REPEATED",
    "name": "futureAppointments",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "customer_notes",
    "type": "STRING"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "company_email",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "company_state",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "company_address",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "company_timezone",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "company_city",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "company_zip",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "company_phone",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "company_name",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "company",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "id",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "timezone",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "valid_email",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "email",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "last_name",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "setter_can_see_office_leads",
            "type": "INTEGER"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "designRevisionSMS",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "dealFeedEmail",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "dealFeedSms",
                "type": "INTEGER"
              }
            ],
            "mode": "NULLABLE",
            "name": "notifications",
            "type": "RECORD"
          },
          {
            "mode": "NULLABLE",
            "name": "can_create_customers",
            "type": "INTEGER"
          },
          {
            "description": "bq-datetime",
            "mode": "NULLABLE",
            "name": "valid_email_ts",
            "type": "TIMESTAMP"
          },
          {
            "mode": "NULLABLE",
            "name": "allow_optimus",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "is_view_only",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "intercom_id",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "sales_rep_license",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "inactive",
            "type": "INTEGER"
          }
        ]
      },
      {
        "mode": "NULLABLE",
        "name": "phone",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "first_name",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "owner",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "fields": [
          {
            "fields": [
              {
                "description": "bq-datetime",
                "mode": "NULLABLE",
                "name": "created_at",
                "type": "TIMESTAMP"
              },
              {
                "description": "bq-datetime",
                "mode": "NULLABLE",
                "name": "updated_at",
                "type": "TIMESTAMP"
              },
              {
                "description": "bq-datetime",
                "mode": "NULLABLE",
                "name": "last_synced",
                "type": "TIMESTAMP"
              },
              {
                "mode": "NULLABLE",
                "name": "enerflo_id",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "record_type",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "integration_record_id",
                "type": "STRING"
              }
            ],
            "mode": "NULLABLE",
            "name": "Lead",
            "type": "RECORD"
          }
        ],
        "mode": "NULLABLE",
        "name": "JobNimbus",
        "type": "RECORD"
      }
    ],
    "mode": "REPEATED",
    "name": "integrations",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "id",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "timezone",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "email",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "last_name",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "phone",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "first_name",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "creator",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "created_by_email",
    "type": "STRING"
  },
  {
    "description": "bq-datetime",
    "mode": "NULLABLE",
    "name": "updated",
    "type": "TIMESTAMP"
  },
  {
    "description": "bq-datetime",
    "mode": "NULLABLE",
    "name": "created",
    "type": "TIMESTAMP"
  },
  {
    "mode": "NULLABLE",
    "name": "id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "last_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "language",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "deleted_at",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "state",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "referral_id",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "fullName",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "lead_router_id",
    "type": "STRING"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "has_valid_email",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "primary_sms_supported",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "location_confirmed",
        "type": "BOOLEAN"
      },
      {
        "mode": "NULLABLE",
        "name": "gmapsOverride",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "nem_override",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "nem_signer",
        "type": "STRING"
      }
    ]
  },
  {
    "mode": "NULLABLE",
    "name": "fullAddress",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "lead_source",
    "type": "STRING"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "sms_number",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "office_state",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "office_tz",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "office_name",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "office_address",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "office_city",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "office_zip",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "office_id",
        "type": "INTEGER"
      }
    ],
    "mode": "NULLABLE",
    "name": "office",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "created_by_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "timezone",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "created_by_phone",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "details",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "agent_id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "external_id",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "city",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "first_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "address",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "secondary_last_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "creator_id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "secondary_first_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "mobile",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "status_name",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "email",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "fullState",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "status_id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "secondary_mobile",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "lng",
    "type": "FLOAT"
  },
  {
    "mode": "NULLABLE",
    "name": "office_id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "lat",
    "type": "FLOAT"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "id",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "timezone",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "valid_email",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "email",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "last_name",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "can_create_customers",
            "type": "INTEGER"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "dealFeedEmail",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "dealFeedSms",
                "type": "INTEGER"
              }
            ],
            "mode": "NULLABLE",
            "name": "notifications",
            "type": "RECORD"
          },
          {
            "mode": "NULLABLE",
            "name": "sales_rep_license",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "inactive",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "allow_optimus",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "is_view_only",
            "type": "INTEGER"
          },
          {
            "description": "bq-datetime",
            "mode": "NULLABLE",
            "name": "valid_email_ts",
            "type": "TIMESTAMP"
          },
          {
            "mode": "NULLABLE",
            "name": "intercom_id",
            "type": "STRING"
          }
        ]
      },
      {
        "mode": "NULLABLE",
        "name": "phone",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "first_name",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "setter",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "zip",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "secondary_email",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "setter_id",
    "type": "INTEGER"
  },
  {
    "mode": "NULLABLE",
    "name": "company_id",
    "type": "INTEGER"
  }
]