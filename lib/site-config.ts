/** 全站统一配置。P0 建立，P1 双语路由后扩展 locale 相关字段。 */

export const SITE_URL = "https://www.leyunke.com";

export const BRAND_ZH = "乐云工具箱";
export const BRAND_EN = "Leyun Tools";
export const BRAND_EN_SHORT = "Leyun";

/** 联系邮箱，全站统一小写显示。 */
export const CONTACT_EMAIL = "tool@leyunke.com";

/** 生成页面自指 canonical。P1 改为带 /zh、/en 前缀。 */
export function canonicalUrl(path = ""): string {
  const clean = path && path !== "/" ? path.replace(/^\//, "") : "";
  return clean ? `${SITE_URL}/${clean}` : `${SITE_URL}/`;
}
