import axios from "axios";
import {PROPERTY_LIST_REQUEST, PROPERTY_LIST_SUCCESS, PROPERTY_LIST_FAIL} from "./types";

export const listProperties = () => async (dispatch) => {
    try {
        dispatch({
            type: PROPERTY_LIST_REQUEST,
        })
        const {data} = await axios.get("/api/v1/properties/all/")

        dispatch({
            type: PROPERTY_LIST_SUCCESS,
            payload: data
        })
    } catch (err) {
        dispatch({
            type: PROPERTY_LIST_FAIL,
            payload: err.response && err.response.data.message ? err.response.data.message : err.message
        })
    }
}