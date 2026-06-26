import { ENDPOINTS, instance } from "../utils/api"
import { SortingCategories } from "../enums";
//import type { SortingCategories } from "../types/sortingCategories";

export default function TopCompaniesTable() {
    async function getTopCompanies(category: string) {
        console.log(category);
        try {
            const response = await instance.get(ENDPOINTS.GET_COMPARISON_DATA(category));
            console.log(response);
        } catch(e) {
            console.log(e);
        };
    };
    return (
        <div>
            <button
                onClick={() => getTopCompanies(SortingCategories.delayed_deliveries_count)}
            >
                Click Me
            </button>
        </div>
    )
}