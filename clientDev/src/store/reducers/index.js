import ProvinceReducer from "./province"
import DistrictReducer from "./district"
import { combineReducers } from "redux"


export default combineReducers({
    provinceR: ProvinceReducer,
    districtR: DistrictReducer
})