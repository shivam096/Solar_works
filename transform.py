def transform(rows):
    return [
        {
            "company_id": row.get("company_id"),
            "office_id": row.get("office_id"),
            "creator_id": row.get("creator_id"),
            "agent_id": row.get("agent_id"),
            "setter_id": row.get("setter_id"),
            "first_name": row.get("first_name"),
            "last_name": row.get("last_name"),
            "email": row.get("email"),
            "mobile": row.get("mobile"),
            "secondary_first_name": row.get("secondary_first_name"),
            "secondary_last_name": row.get("secondary_last_name"),
            "secondary_mobile": row.get("secondary_mobile"),
            "secondary_email": row.get("secondary_email"),
            "address": row.get("address"),
            "city": row.get("city"),
            "state": row.get("state"),
            "zip": row.get("zip"),
            "lat": row.get("lat"),
            "lng": row.get("lng"),
            "timezone": row.get("timezone"),
            "details": row.get("details"),
            "external_id": row.get("external_id"),
            "lead_source": row.get("lead_source"),
            "status_id": row.get("status_id"),
            "lead_router_id": row.get("lead_router_id"),
            "referral_id": row.get("referral_id"),
            "deleted_at": row.get("deleted_at"),
            "language": row.get("language"),
            "fullName": row.get("fullName"),
            "id": row.get("id"),
            "created": row.get("created"),
            "updated": row.get("updated"),
            "fullState": row.get("fullState"),
            "fullAddress": row.get("fullAddress"),
            "status_name": row.get("status_name"),
            "created_by_name": row.get("created_by_name"),
            "created_by_email": row.get("created_by_email"),
            "created_by_phone": row.get("created_by_phone"),
            "creator": {
                "first_name": row["creator"].get("first_name"),
                "last_name": row["creator"].get("last_name"),
                "email": row["creator"].get("email"),
                "phone": row["creator"].get("phone"),
                "timezone": row["creator"].get("timezone"),
                "id": row["creator"].get("id"),
            }
            if row.get("creator")
            else {},
            "integrations": {
                "JobNimbus": {
                    "Lead": {
                        "integration_record_id": row["integrations"]["JobNimbus"][
                            "Lead"
                        ].get("integration_record_id"),
                        "record_type": row["integrations"]["JobNimbus"]["Lead"].get(
                            "record_type"
                        ),
                        "enerflo_id": row["integrations"]["JobNimbus"]["Lead"].get(
                            "enerflo_id"
                        ),
                        "last_synced": row["integrations"]["JobNimbus"]["Lead"].get(
                            "last_synced"
                        ),
                        "updated_at": row["integrations"]["JobNimbus"]["Lead"].get(
                            "updated_at"
                        ),
                        "created_at": row["integrations"]["JobNimbus"]["Lead"].get(
                            "created_at"
                        ),
                    }
                    if row["integrations"]["JobNimbus"].get("Lead")
                    else {},
                }
                if row["integrations"].get("JobNimbus")
                else {}
            }
            if row.get("integrations")
            else {},
            "owner": {
                "first_name": row["owner"].get("first_name"),
                "last_name": row["owner"].get("last_name"),
                "email": row["owner"].get("email"),
                "valid_email": row["owner"].get("valid_email"),
                "phone": row["owner"].get("phone"),
                "timezone": row["owner"].get("timezone"),
                "id": row["owner"].get("id"),
                "meta": {
                    "inactive": row["owner"]["meta"].get("inactive"),
                    "intercom_id": row["owner"]["meta"].get("intercom_id"),
                    "is_view_only": row["owner"]["meta"].get("is_view_only"),
                    "allow_optimus": row["owner"]["meta"].get("allow_optimus"),
                    "valid_email_ts": row["owner"]["meta"].get("valid_email_ts"),
                    "sales_rep_license": row["owner"]["meta"].get("sales_rep_license"),
                    "can_create_customers": row["owner"]["meta"].get(
                        "can_create_customers"
                    ),
                }
                if row["owner"].get("meta")
                else {},
            }
            if row.get("owner")
            else {},
            "office": {
                "office_name": row["office"].get("office_name"),
                "office_id": row["office"].get("office_id"),
                "office_city": row["office"].get("office_city"),
                "office_address": row["office"].get("office_address"),
                "office_zip": row["office"].get("office_zip"),
                "office_tz": row["office"].get("office_tz"),
                "office_state": row["office"].get("office_state"),
                "sms_number": row["office"].get("sms_number"),
            },
            "company": {
                "company_name": row["company"].get("company_name"),
                "company_phone": row["company"].get("company_phone"),
                "company_address": row["company"].get("company_address"),
                "company_city": row["company"].get("company_city"),
                "company_state": row["company"].get("company_state"),
                "company_zip": row["company"].get("company_zip"),
                "company_email": row["company"].get("company_email"),
                "company_timezone": row["company"].get("company_timezone"),
            },
            "customer_notes": row.get("customer_notes"),
            "customer_portal_url": row.get("customer_portal_url"),
            "surveys": {
                "solar_works_deal": {
                    "name": row["surveys"]["Solar Works Deal"].get("name"),
                    "type": row["surveys"]["Solar Works Deal"].get("type"),
                    "id": row["surveys"]["Solar Works Deal"].get("id"),
                    "install": {
                        "id": row["surveys"]["Solar Works Deal"]["install"].get("id"),
                        "status": row["surveys"]["Solar Works Deal"]["install"].get(
                            "status"
                        ),
                        "created_at": row["surveys"]["Solar Works Deal"]["install"].get(
                            "created_at"
                        ),
                        "updated_at": row["surveys"]["Solar Works Deal"]["install"].get(
                            "updated_at"
                        ),
                    }
                    if row["surveys"]["Solar Works Deal"].get("install")
                    else {},
                },
                "Solar_Works_Optimus_or_SPS_Deal": {
                    "name": row["surveys"]["Solar Works Deal"].get("name"),
                    "type": row["surveys"]["Solar Works Deal"].get("type"),
                    "id": row["surveys"]["Solar Works Deal"].get("id")
                },
                "Solar_Works_Site_Survey": {
                    "name": row["surveys"]["Solar Works Deal"].get("name"),
                    "type": row["surveys"]["Solar Works Deal"].get("type"),
                    "id": row["surveys"]["Solar Works Deal"].get("id")
                },
            },
        }
        for row in rows
    ]