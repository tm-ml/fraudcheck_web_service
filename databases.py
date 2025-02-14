from datetime import datetime, date

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date, DateTime



#Create database:
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class ClaimDataTable(db.Model):
    __tablename__ = "claim_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Add foreign keys:
    driver_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("driver_table.id"))
    vehicle_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("vehicle_table.id"))
    policy_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("policy_table.id"))
    collision_date: Mapped[date] = mapped_column(Date, nullable=False)
    claim_report_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    accident_area: Mapped[str] = mapped_column(String(250), nullable=False)
    fault: Mapped[str] = mapped_column(String(250), nullable=False)
    police_report: Mapped[str] = mapped_column(String(250), nullable=False)
    witness_present: Mapped[str] = mapped_column(String(250), nullable=False)
    address_change_claim: Mapped[str] = mapped_column(String(250), nullable=False)
    # Add relations:
    driver: Mapped["DriverDataTable"] = relationship("DriverDataTable", back_populates="claims")
    vehicle: Mapped["VehicleDataTable"] = relationship("VehicleDataTable", back_populates="claims")
    policy: Mapped["PolicyDataTable"] = relationship("PolicyDataTable", back_populates="claims")

class DriverDataTable(db.Model):
    __tablename__ = "driver_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sex: Mapped[str] = mapped_column(String(250), nullable=False)
    marital_status: Mapped[str] = mapped_column(String(250), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    driver_rating: Mapped[int] = mapped_column(Integer, nullable=False)
    past_number_of_claim: Mapped[int] = mapped_column(Integer, nullable=False)
    number_of_cars: Mapped[int] = mapped_column(Integer, nullable=False)
    # Add relation:
    claims: Mapped[list["ClaimDataTable"]] = relationship("ClaimDataTable", back_populates="driver")

class VehicleDataTable(db.Model):
    __tablename__ = "vehicle_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    make: Mapped[str] = mapped_column(String(250), nullable=False)
    vehicle_category: Mapped[str] = mapped_column(String(250), nullable=False)
    year_of_production: Mapped[int] = mapped_column(Integer, nullable=False) # TODO use to calculate age_of_vehicle
    # Add relation:
    claims: Mapped[list["ClaimDataTable"]] = relationship("ClaimDataTable", back_populates="vehicle")

class PolicyDataTable(db.Model):
    __tablename__ = "policy_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    policy_number: Mapped[str] = mapped_column(String(250), nullable=False)
    deductible: Mapped[str] = mapped_column(String(250), nullable=False)
    base_policy: Mapped[str] = mapped_column(String(250), nullable=False)
    agent_type: Mapped[str] = mapped_column(String(250), nullable=False)
    number_of_supplements: Mapped[int] = mapped_column(Integer, nullable=False)
    age_of_policy_holder: Mapped[int] = mapped_column(Integer, nullable=False)

    # Add relation:
    claims: Mapped[list["ClaimDataTable"]] = relationship("ClaimDataTable", back_populates="policy")