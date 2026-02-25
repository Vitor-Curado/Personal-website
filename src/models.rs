use serde::Serialize;

#[derive(Serialize)]
pub struct Food {
    pub title: &'static str,
    pub slug: &'static str,
    pub image_gallery: Vec<&'static str>,
    pub main_ingredients: Vec<&'static str>,
    pub cooking_method: &'static str,
    pub equipment: Vec<&'static str>,
    pub estimated_time_required_in_minutes: u32,
    pub one_serving_visual_reference: &'static str,
    pub one_serving_weight_reference_in_grams: u32,
    
    pub health_profile: &'static str,
    pub preparation_difficulty: &'static str,
    pub cooking_instructions: Vec<&'static str>,
    pub diet_friendly_to: Vec<&'static str>,
}